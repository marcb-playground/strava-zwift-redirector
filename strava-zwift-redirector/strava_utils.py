# strava_utils.py
import requests
from datetime import datetime
from stravalib import Client
import urllib3
from flask import request, jsonify

def get_strava_client(client_id,client_secret,refresh_token):
   
    access_token = get_access_token(client_id,client_secret,refresh_token)
    print("getting strava client")
    client = Client(access_token=access_token)
    return client

def get_refresh_token(client_id,client_secret,code_from_redirect):
    urllib3.disable_warnings()
    print("getting client token")
    auth_url ="https://www.strava.com/oauth/token"
    payload = {
        'client_id' : client_id,
        'client_secret' : client_secret,
        'code' : code_from_redirect,
        'grant_type' : "authorization_code",
        'f':'json'
    }
    print("Requesting the token...\n")
    res = requests.post(auth_url,data=payload,verify=False)
    print(res.json())
    print()

    try:
        refresh_token = res.json()['refresh_token']
        expiry_ts = res.json()['expires_at']
    except Exception as err:
        raise(f"Failed get get refresh token: {err}")
    print("New token will expire at: ",end='\t')
    print(datetime.utcfromtimestamp(expiry_ts).strftime('%Y-%m-%d %H:%M:%S'))
    return refresh_token

def get_access_token(client_id,client_secret,refresh_token):
    """
    Need to authorize scope 
    https://www.strava.com/oauth/authorize?client_id=60066&response_type=code&redirect_uri=http://localhost:8085&scope=activity:read_all
    """
    urllib3.disable_warnings()
    print("getting client token")
    auth_url ="https://www.strava.com/oauth/token"
    payload = {
        'client_id' : client_id,
        'client_secret' : client_secret,
        'refresh_token' : refresh_token,
        'grant_type' : "refresh_token",
        'f':'json'
    }
    print("Requesting the token...\n")
    res = requests.post(auth_url,data=payload,verify=False)
    print(res.json())
    print()

    try:
        access_token = res.json()['access_token']
        expiry_ts = res.json()['expires_at']
    except Exception as err:
        raise(f"Failed get get access token: {err}")
    print("New token will expire at: ",end='\t')
    print(datetime.utcfromtimestamp(expiry_ts).strftime('%Y-%m-%d %H:%M:%S'))
    return access_token

def fetch_activity_detail(client, activity_id):
    try:
        return client.get_activity(activity_id)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch activity: {e}")
    
def fetch_activities(client, limit=10):
    try:
        return client.get_activities(limit=limit)
    except Exception as e:
        raise RuntimeError(f"Failed to get activites : {e}")
    


def subscribe_to_strava_push(subscription_url, client_id, client_secret, callback_url):
    #headers = {'Authorization': f'Bearer {client.access_token}'}
    random_token = "elwkmgklewklm"
    #subscribe
    payload = {
        'client_id' : client_id,
        'client_secret' : client_secret,
        'callback_url' : callback_url,
        'verify_token' : random_token
    }
    print("Subscribe info: " + str(payload))
    response = requests.post(subscription_url, data=payload)
    print(str(response))
    if response.status_code == 200:
        print("success subscribe: \n" + str(response.text))
    else:
        
        raise Exception("failed to subscribe")


    # # validate
    # payload = {
    #     #'hub.callback': callback_url,
    #     'hub.mode': 'subscribe',
    #     'hub.verify_token': random_token,
    #     'hub.topic': ""
    # }
    # print("verify info: " + str(payload))
    # response = requests.post(subscription_url, data=payload)

    # if response.status_code == 200:
    #     print(str(response))
    #     return jsonify({'message': 'Subscription successful. Sub id ' + str(response.json()['id'])}), 200
    # else:
    #     return jsonify({'error': 'Failed to subscribe', 'details': response.json()}), response.status_code
