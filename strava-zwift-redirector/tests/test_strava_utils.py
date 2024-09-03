# tests/test_strava_utils.py
import pytest, os
from strava_utils import get_strava_client, fetch_activity, subscribe_to_strava_push
from stravalib import Client
STRAVA_SOURCE_CLIENT_ID = os.getenv('STRAVA_SOURCE_CLIENT_ID')
STRAVA_SOURCE_CLIENT_SECRET = os.getenv('STRAVA_SOURCE_CLIENT_SECRET')
STRAVA_SOURCE_REFRESH_TOKEN = os.getenv('STRAVA_SOURCE_REFRESH_TOKEN')


@pytest.fixture
def mock_client(mocker):
    mock_client = mocker.patch.object(Client, 'get_activity')
    return mock_client

@pytest.fixture
def strava_client():
    
    return get_strava_client(client_id=STRAVA_SOURCE_CLIENT_ID,
                               client_secret=STRAVA_SOURCE_CLIENT_SECRET,
                               refresh_token=STRAVA_SOURCE_REFRESH_TOKEN)
    
def test_get_strava_client(strava_client):
    
    assert strava_client.access_token is not None

def test_fetch_activity_success(mock_client):
    mock_client.return_value = {'average_watts': 200}
    client = get_strava_client('test_token')
    activity = fetch_activity(client, 123)
    assert activity['average_watts'] == 200

def test_fetch_activity_failure(mocker):
    mock_client = mocker.patch('stravalib.Client.get_activity', side_effect=Exception('error'))
    client = get_strava_client('test_token')
    with pytest.raises(RuntimeError):
        fetch_activity(client, 123)

def test_subscribe_to_strava_push(strava_client):
    STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL = os.getenv('WEBHOOK_CALLBACK_URL')
    subscription_url = 'https://www.strava.com/api/v3/push_subscriptions'
    try:
        subscribe_to_strava_push(subscription_url=subscription_url, 
                                        client_id=STRAVA_SOURCE_CLIENT_ID, 
                                        client_secret=STRAVA_SOURCE_CLIENT_SECRET,
                                        callback_url= STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL)
        
        assert 1 == 1
    except Exception as err:
        print("test failed")
        assert 0 == 1