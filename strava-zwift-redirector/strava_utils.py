# strava_utils.py
import requests
from datetime import datetime
from stravalib import Client
import urllib3


def get_strava_client(client_id,client_secret,refresh_token):
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

    access_token = res.json()['access_token']
    expiry_ts = res.json()['expires_at']
    print("New token will expire at: ",end='\t')
    print(datetime.utcfromtimestamp(expiry_ts).strftime('%Y-%m-%d %H:%M:%S'))

    print("getting strava client")
    client = Client()
    client.access_token = access_token
    return client

def fetch_activity(client, activity_id):
    try:
        return client.get_activity(activity_id)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch activity: {e}")