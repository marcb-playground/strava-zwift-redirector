# app.py
from flask import Flask, request, jsonify
import os
from strava_utils import get_strava_client, subscribe_to_strava_push
from webhook_handler import handle_strava_notification, verify_webhook

app = Flask(__name__)

# Load environment variables
STRAVA_SOURCE_CLIENT_ID = os.getenv('STRAVA_SOURCE_CLIENT_ID')
STRAVA_SOURCE_CLIENT_SECRET = os.getenv('STRAVA_SOURCE_CLIENT_SECRET')
STRAVA_SOURCE_REFRESH_TOKEN = os.getenv('STRAVA_SOURCE_REFRESH_TOKEN')
#STRAVA_DESTINATION_ACCESS_TOKEN = os.getenv('STRAVA_DESTINATION_ACCESS_TOKEN')
WATTAGE_THRESHOLD = float(100)  # Default threshold
STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL = os.getenv('WEBHOOK_CALLBACK_URL')  # e.g., "https://yourdomain.com/webhook"

source_client = get_strava_client(client_id=STRAVA_SOURCE_CLIENT_ID,
                               client_secret=STRAVA_SOURCE_CLIENT_SECRET,
                               refresh_token=STRAVA_SOURCE_REFRESH_TOKEN)

@app.route('/strava_notification', methods=['POST'])
def strava_notification():
    data = request.json
    return handle_strava_notification(data, source_client, STRAVA_DESTINATION_ACCESS_TOKEN, WATTAGE_THRESHOLD)

@app.route('/strava_notification', methods=['GET'])
def verify():
    hub_mode = request.args.get('hub.mode')
    hub_challenge = request.args.get('hub.challenge')
    hub_verify_token = request.args.get('hub.verify_token')
    return verify_webhook(hub_mode, hub_challenge, hub_verify_token, source_client)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    print(f"Subscribing for {STRAVA_SOURCE_CLIENT_ID}")
    subscription_url = 'https://www.strava.com/api/v3/push_subscriptions'
    return subscribe_to_strava_push(subscription_url=subscription_url, 
                                    client=source_client, 
                                    callback_url= STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL)

if __name__ == '__main__':
    app.run(debug=True)
