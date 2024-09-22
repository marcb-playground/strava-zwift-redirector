# app.py
from flask import Flask, request, jsonify
import os
from .strava_client import StravaClient
import logging
import time
from .strava_utils import (
    get_strava_client,
    subscribe_to_strava_push,
    move_activity_to_user,
    fetch_activities
)
from .webhook_handler import handle_strava_notification
import asyncio
import threading
# CONSTANTS
WATTAGE_THRESHOLD = float(100)  # Default threshold
STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL = "https://strava-zwift-redirector.vercel.app/strava-notification"  # e.g., "https://yourdomain.com/webhook"

app = Flask(__name__)


@app.route("/")
def home():
    print("main page visited")
    return "Hello, World!"


@app.route("/strava-client-info")
def client():

    source_client = StravaClient(client_for="source")
    athlete_firstname = str(source_client.stravalib_client.get_athlete().firstname)
    print(f"checked {athlete_firstname}")
    return jsonify({"athlete firstname": athlete_firstname}), 200

@app.route("/switch-zwift")
@app.route("/switch-zwift/<int:activities_to_skip>")
def switch_zwift(activities_to_skip=1):
    print(f"loading source client")
    source_client = StravaClient(client_for="source")
    latest_activities = fetch_activities(
        client=source_client, limit=activities_to_skip
    )
    *_, last_activity = latest_activities
    print(f"last activity detected : {last_activity.name}")
    print(f"loading target client")

    # try to wait to fix client id issue
    target_client = StravaClient(client_for="target")
    print(f"loaded target client")
    
    new_activity_id = move_activity_to_user(
        source_client=source_client,
        source_activity_id=last_activity.id,
        target_client=target_client,
        wattage_threshold=WATTAGE_THRESHOLD,
    )
    if new_activity_id is not None:
        msg = f'moved activity {last_activity.name} with id {new_activity_id}'
    else:
        msg = "Wattage threshold for {last_activity.name} was not met, did not copy over file."
    print(msg)
    return msg, 200



@app.route("/strava-notification", methods=["GET"])
def verify():
    print(f"callback GET for subscription challenge initiated ")

    hub_mode = request.args.get("hub.mode")
    hub_challenge = request.args.get("hub.challenge")
    hub_verify_token = request.args.get("hub.verify_token")

    if hub_mode == "subscribe":
        print(f"verifying subscription to {hub_verify_token} with {hub_challenge}")
        return jsonify({"hub.challenge": hub_challenge}), 200
    else:
        print("not subscribe mode")
        return jsonify({"error": "Verification failed"}), 403


def run_user_activity_move(activity_id):
    
    source_client = StravaClient(client_for="source")
    target_client = StravaClient(client_for="target")
    asyncio.run(
        move_activity_to_user(
            source_client=source_client,
            target_client=target_client,
            source_activity_id=activity_id,
            wattage_threshold=WATTAGE_THRESHOLD
        )
    )

@app.route("/strava-notification", methods=["POST"])
def process_notification():
    print("received notification POST! an activity is coming in...")
    try:
        object_type = request.args.get("object_type")  # should be activity
        object_id = request.args.get("object_id")  # activity id to pass for transfer
        aspect_type = request.args.get("aspect_type")  # we want only for create
        if object_type == "activity" and aspect_type == "create":
            print(f"received activity with id: {object_id}")
            threading.Thread(target=run_user_activity_move, args=(object_id,)).start()
            return jsonify({"received activity": str(object_id)}), 200
        else:
            print(f"received PUSH that we are not processing: \n{object_type} \n {object_id} \n {aspect_type}")
            return "ignoring this", 200
    except RuntimeError as err:

        return jsonify({"failed to parse webhook error ": str(err)}), 500


@app.route("/subscribe")
def subscribe():
    source_client = StravaClient(client_for="source")
    print(f"Subscribing for {source_client.client_id}")
    subscription_url = "https://www.strava.com/api/v3/push_subscriptions"
    return subscribe_to_strava_push(
        subscription_url=subscription_url,
        client_id=source_client.client_id,
        client_secret=source_client.client_secret,
        callback_url=STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL,
    )


if __name__ == "__main__":
    app.run(debug=True)
