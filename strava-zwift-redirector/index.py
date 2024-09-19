# app.py
from flask import Flask, request, jsonify
import os
from .strava_client import StravaClient
import logging
#import strava_utils
from .strava_utils import get_strava_client, subscribe_to_strava_push
from .webhook_handler import handle_strava_notification, verify_webhook

# CONSTANTS
WATTAGE_THRESHOLD = float(100)  # Default threshold
STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL = "https://strava-zwift-redirector.vercel.app/strava-notification"  # e.g., "https://yourdomain.com/webhook"

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/")
def home():
    logger.info("main page visited")
    return "Hello, World!"


@app.route("/strava-client-info")
def client():

    source_client = StravaClient(client_for="source")
    athlete_firstname = str(source_client.stravalib_client.get_athlete().firstname)
    logger.info(f"checked {athlete_firstname}")
    return jsonify({'athlete firstname': athlete_firstname}), 200


@app.route('/strava-notification', methods=['GET'])
def verify():
    source_client = StravaClient(client_for="source")
    hub_mode = request.args.get('hub.mode')
    hub_challenge = request.args.get('hub.challenge')
    hub_verify_token = request.args.get('hub.verify_token')
    return verify_webhook(hub_mode, hub_challenge, hub_verify_token, source_client)

@app.route('/strava-notification', methods=['POST'])
def process_notification():
    
    try:
        object_type = request.args.get('object_type') #should be activity
        object_id = request.args.get('object_id') #activity id to pass for transfer
        aspect_type = request.args.get('aspect_type') #we want only for create
    except RuntimeError as err:
        return jsonify({'failed to parse webhook error ': str(err)}), 500
        

@app.route('/subscribe', methods=['POST'])
def subscribe():
    source_client = StravaClient(client_for="source")
    print(f"Subscribing for {source_client.client_id}")
    subscription_url = 'https://www.strava.com/api/v3/push_subscriptions'
    return subscribe_to_strava_push(subscription_url=subscription_url,
                                    client=source_client,
                                    callback_url= STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL)

if __name__ == "__main__":
    app.run(debug=True)
