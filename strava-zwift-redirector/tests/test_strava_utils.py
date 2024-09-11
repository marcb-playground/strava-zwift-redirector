# tests/test_strava_utils.py
import pytest, os
import strava_utils
STRAVA_SOURCE_CLIENT_ID = os.getenv('STRAVA_SOURCE_CLIENT_ID')
STRAVA_SOURCE_CLIENT_SECRET = os.getenv('STRAVA_SOURCE_CLIENT_SECRET')
STRAVA_SOURCE_REFRESH_TOKEN = os.getenv('STRAVA_SOURCE_REFRESH_TOKEN')

@pytest.fixture
def strava_client():
    
    return strava_utils.get_strava_client(client_id=STRAVA_SOURCE_CLIENT_ID,
                               client_secret=STRAVA_SOURCE_CLIENT_SECRET,
                               refresh_token=STRAVA_SOURCE_REFRESH_TOKEN)
    
def test_get_strava_client(strava_client):
    
    assert strava_client.access_token is not None

def test_fetch_activities(strava_client):

    refresh_token = "GET FROM NEW TOKEN"

    api_client = strava_utils.get_strava_client(client_id=STRAVA_SOURCE_CLIENT_ID,
                               client_secret=STRAVA_SOURCE_CLIENT_SECRET,
                               #refresh_token=STRAVA_SOURCE_REFRESH_TOKEN)
                               refresh_token=refresh_token)

    latest_activities = strava_utils.fetch_activities(client=api_client,limit=1)
    print(str(latest_activities))
    activity_ids = [activity.id for activity in latest_activities]
    assert len(activity_ids) == 1

def test_fetch_activity_detail():

    
    latest_activity = strava_utils.fetch_activity_detail()
    activity = strava_utils.fetch_activity(strava_client, 123)
    print(str(activity))
    assert activity['average_watts'] != 0

def test_get_refresh_token():
    ## TO FIX!!
    """
    Need to authorize scope 
    https://www.strava.com/oauth/authorize?client_id=60066&response_type=code&redirect_uri=http://localhost:8085&scope=activity:read_all
    """
    auth_code = "get auth code from above URI to reset a new auth code"

    #refresh_token = strava_utils.get_refresh_token_from_refresh(client_id=STRAVA_SOURCE_CLIENT_ID,
    #                           client_secret=STRAVA_SOURCE_CLIENT_SECRET,
    #                          refresh_token=STRAVA_SOURCE_REFRESH_TOKEN)
    
    #assert refresh_token is not None

    refresh_token = strava_utils.get_refresh_token_from_auth_code(client_id=STRAVA_SOURCE_CLIENT_ID,
                               client_secret=STRAVA_SOURCE_CLIENT_SECRET,
                               auth_code=auth_code)
    
    assert refresh_token is not None


def test_get_access_token():
    refresh_token = "stored user refresh token"

    access_token = strava_utils.get_access_token(client_id=STRAVA_SOURCE_CLIENT_ID,
                               client_secret=STRAVA_SOURCE_CLIENT_SECRET,
                               refresh_token=refresh_token)
    
    assert access_token is not None

def test_subscribe_to_strava_push(strava_client):
    STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL = os.getenv('WEBHOOK_CALLBACK_URL')
    subscription_url = 'https://www.strava.com/api/v3/push_subscriptions'
    try:
        strava_utils.subscribe_to_strava_push(subscription_url=subscription_url, 
                                        client_id=STRAVA_SOURCE_CLIENT_ID, 
                                        client_secret=STRAVA_SOURCE_CLIENT_SECRET,
                                        callback_url= STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL)
        
        assert 1 == 1
    except Exception as err:
        print("test failed")
        assert 0 == 1