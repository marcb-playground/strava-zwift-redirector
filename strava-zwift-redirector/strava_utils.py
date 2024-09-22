# strava_utils.py
import requests, os
from datetime import datetime
from stravalib import Client
import urllib3
from pathlib import Path
from strava2gpx import strava2gpx
import asyncio
from datetime import datetime
from xml_utils import move_watts_to_power
import xml_utils
import logging
import jsonify

logger = logging.getLogger(__name__)

def move_activity_to_user(source_client,source_activity_id,target_client,wattage_threshold):
    """Take an activity from source client, upload it to target and delete if it meets threshold"""

    logger.info(f"getting source activity {source_activity_id}")
    activity_in_scope = source_client.stravalib_client.get_activity(source_activity_id)

    if activity_in_scope.average_watts < wattage_threshold:
        logger.info(f"detected activity under {wattage_threshold} so will try to move to user and delete")
         
        now = datetime.now()

        # Format the date and time
        formatted_date_time = now.strftime("%y%m%d%H%M%S")
        tmp_output_path = f"/tmp/athlete_fit_file_{formatted_date_time}"

        asyncio.run(save_activity_file(
            client_id=source_client.client_id,
            client_secret=source_client.client_secret,
            refresh_token=source_client.client_refresh_token,
            activity_id=activity_in_scope.id,
            output_path=tmp_output_path,
        ))
        # await save_activity_file(
        #     client_id=source_client.client_id,
        #     client_secret=source_client.client_secret,
        #     refresh_token=source_client.client_refresh_token,
        #     activity_id=activity_in_scope.id,
        #     output_path=tmp_output_path,
        # )
        

        file_path = Path(f"{tmp_output_path}.gpx")

        assert file_path.is_file(), f"File '{file_path}' does not exist."
        move_watts_to_power(
            file_source_path=file_path, file_target_path=file_path
        )

        # this target client ends up with bad secret?
        new_activity_id = upload_activity_file(
            target_client.stravalib_client, file_path, activity_in_scope.name
        )
        
        if new_activity_id is not None:
            logger.info("detected new activity upload successfull. need to delete from source")
            # SHOULD CLEANUP TEMP FILE HERE TOO
            # strava removed the delete from API so need to do manually
            #source_client.stravalib_client.delete_activity(source_activity_id)
            return new_activity_id
        else:
            raise Exception(f"Issue uploading {activity_in_scope.name} {file_path}")
    else:
        print("activity did not meet threshold, not moving")
        return None



async def save_activity_file(client_id, client_secret, refresh_token, activity_id, output_path):
    """Fetches activity data from Strava and saves it as a .fit file."""
    # activity = client.get_activity(activity_id)

    # Fetch the activity file (usually .fit or .tcx format)
    # https://www.strava.com/activities/{activity_id}/export_original
    #fit_file_url = f"https://www.strava.com/activities/{activity_id}/export_original"
    #fit files can only get from login page

    # create an instance of strava2gpx
    logger.info("attempting to create gpx file")
    s2g = strava2gpx(client_id, client_secret, refresh_token)

    # connect to Strava API
    await s2g.connect()

    try:
        Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
    except Exception as err:
        raise RuntimeError(f"Failed to create dir for fit storage: {err}")
    # Download the file
    print(f"attempting to download file")
    # write activity to output.gpx by activity id
    await s2g.write_to_gpx(activity_id, output_path)

    print(f"file at: {output_path}")
    return output_path

def upload_activity_file(client, file_path, activity_name):
    """Uploads activity data to Strava to given stravalib client."""
    logger.info(f"uploading activity from {file_path}")
    try:
        with open(file_path, "rb") as file:
            activity = client.upload_activity(
                activity_file=file,
                name=activity_name,
                description="auto uploaded from zwift redirector",
                data_type="gpx"
                # activity_type="VirtualRide",
                # trainer=1
            )
        detailed_activity = activity.wait()
        logger.info(f"uploaded activity: {str(detailed_activity.name)}")
        return detailed_activity.upload_id
    except Exception as err:
        raise RuntimeError(f"Could not upload file: {err}")


def get_strava_client(client_id, client_secret, refresh_token):
    access_token = get_access_token(client_id, client_secret, refresh_token)
    print("getting strava client")
    client = Client(access_token=access_token)
    return client


def get_refresh_token_from_auth_code(client_id, client_secret, auth_code):
    """to get auth code https://www.strava.com/oauth/authorize?client_id=60066&response_type=code&redirect_uri=http://localhost:8085&scope=activity:read_all"""
    urllib3.disable_warnings()
    print("getting client token")
    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "grant_type": "authorization_code",
        "f": "json",
    }
    print("Requesting the token...\n")
    response = requests.post(auth_url, data=payload, verify=False)
    #print(response.json())
    #print()
    if response.status_code == 200:
        print("success getting token")
    else:

        raise Exception("failed to call")
    try:
        refresh_token = response.json()["refresh_token"]
        # expiry_ts = res.json()['expires_at']
    except Exception as err:
        raise RuntimeError(f"Failed get get refresh token: {err}")
    print("New token will expire at: ", end="\t")
    # print(datetime.utcfromtimestamp(expiry_ts).strftime('%Y-%m-%d %H:%M:%S'))
    return refresh_token


def get_refresh_token_from_refresh(client_id, client_secret, refresh_token):
    urllib3.disable_warnings()
    print("getting client token")
    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
        "f": "json",
    }
    print("Requesting the token...\n")
    response = requests.post(auth_url, data=payload, verify=False)
    #print(response.json())
    #print()
    if response.status_code == 200:
        print("success getting token")
    else:

        raise Exception("failed to call")
    try:
        refresh_token = response.json()["refresh_token"]
        # expiry_ts = res.json()['expires_at']
    except Exception as err:
        raise RuntimeError(f"Failed get get refresh token: {err}")
    print("New token will expire at: ", end="\t")
    # print(datetime.utcfromtimestamp(expiry_ts).strftime('%Y-%m-%d %H:%M:%S'))
    return refresh_token


def get_access_token(client_id, client_secret, refresh_token):
    """
    Need to authorize scope
    https://www.strava.com/oauth/authorize?client_id=60066&response_type=code&redirect_uri=http://localhost:8085&scope=activity:read_all
    """
    urllib3.disable_warnings()
    print("getting client token")
    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
        "f": "json",
    }
    print(str(payload))
    print(f"Requesting the token for {client_id}...\n")
    response = requests.post(auth_url, data=payload, verify=False)
    print(f"received: {response.json()}")
    #print()
    if response.status_code == 200:
        print("success getting token")
    else:

        raise Exception(f"failed to call with response: {response}")
    try:
        access_token = response.json()["access_token"]
        expiry_ts = response.json()["expires_at"]
    except Exception as err:
        raise RuntimeError(f"Failed get get access token: {err}")
    print("New token will expire at: ", end="\t")
    print(datetime.utcfromtimestamp(expiry_ts).strftime("%Y-%m-%d %H:%M:%S"))
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
    # headers = {'Authorization': f'Bearer {client.access_token}'}
    verify_token = "STRAVA-ZWIFT-REDIRECTOR"
    # subscribe
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "callback_url": callback_url,
        "verify_token": verify_token,
    }
    print("Subscribing for client id: " + str(client_id))
    response = requests.post(subscription_url, data=payload)
    
    if response.status_code == 200:
        print("success subscribe: \n" + str(response.text))
        return jsonify({'response': response.text}), 200
    else:
        print(f"failed to subscribe: {response.text}")
        raise Exception("failed to subscribe")

def view_subscriptions(subscription_url, client_id, client_secret):
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
    }
    print("Subscribing for client id: " + str(client_id))
    response = requests.get(subscription_url, params=payload)
    
    if response.status_code == 200:
        print("success subscribe: \n" + str(response.text))
    else:
        raise Exception(f"failed to view subscriptions {str(response.text)}")