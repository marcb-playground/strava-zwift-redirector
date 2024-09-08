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

    latest_activities = strava_utils.fetch_activities(client=strava_client,limit=1)
    print(str(latest_activities))
    activity_ids = [activity.id for activity in latest_activities]
    assert len(activity_ids) == 1

def test_fetch_activity_detail(strava_client):
    latest_activity = strava_utils.fetch_activity_detail()
    activity = strava_utils.fetch_activity(strava_client, 123)
    print(str(activity))
    assert activity['average_watts'] != 0

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