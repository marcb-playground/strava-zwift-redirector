# webhook_handler.py
import requests
from flask import request, jsonify
from strava_utils import fetch_activity

def handle_strava_notification(data, source_client, destination_access_token, wattage_threshold):
    if not data:
        return jsonify({'error': 'No data received'}), 400

    activity_id = data.get('object_id')
    if not activity_id:
        return jsonify({'error': 'No activity ID provided'}), 400

    # Fetch activity details using stravalib
    try:
        activity = fetch_activity(source_client, activity_id)
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500
    file_path = None
    #TODO
    #file_path = create_file_from_activity(activity)

    wattage = activity.average_watts

    if wattage < wattage_threshold:
        # Upload activity to the destination Strava account
        upload_url = 'https://www.strava.com/api/v3/uploads'
        files = {'file': open(file_path, 'rb')}
        payload = {
            'activity_type': 'ride',
            'data_type': 'fit',
        }
        headers = {'Authorization': f'Bearer {destination_access_token}'}
        response = requests.post(upload_url, files=files, data=payload, headers=headers)

        if response.status_code == 201:
            return jsonify({'message': 'Activity uploaded successfully'}), 201
        else:
            return jsonify({'error': 'Failed to upload activity'}), 500

    return jsonify({'message': 'Wattage meets or exceeds the threshold'}), 200

def verify_webhook(hub_mode, hub_challenge, hub_verify_token, client_id):
    if hub_mode == 'subscribe':
        return hub_challenge
    else:
        return jsonify({'error': 'Verification failed'}), 403

def subscribe_to_webhook(subscription_url, client_id, client_secret, callback_url):
    headers = {'Authorization': f'Bearer {access_token}'}
    
    #subscribe
    response = 

    # validate
    payload = {
        'hub.callback': callback_url,
        'hub.mode': 'subscribe',
        'hub.verify_token': access_token,
        'hub.topic': ""
    }
    print("Subscribe info: " + str(payload))
    response = requests.post(subscription_url, headers=headers, data=payload)

    if response.status_code == 200:
        print(string(response))
        return jsonify({'message': 'Subscription successful'}), 200
    else:
        return jsonify({'error': 'Failed to subscribe', 'details': response.json()}), response.status_code

# def subscribe_to_webhook(subscription_url, access_token, callback_url):
#     headers = {'Authorization': f'Bearer {access_token}'}
#     payload = {
#         'hub.callback': callback_url,
#         'hub.mode': 'subscribe',
#         'hub.verify_token': access_token,
#         'hub.topic': ""
#     }
#     print("Subscribe info: " + str(payload))
#     response = requests.post(subscription_url, headers=headers, data=payload)

#     if response.status_code == 200:
#         print(string(response))
#         return jsonify({'message': 'Subscription successful'}), 200
#     else:
#         return jsonify({'error': 'Failed to subscribe', 'details': response.json()}), response.status_code
