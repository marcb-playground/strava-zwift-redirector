# tests/test_strava_utils.py
import pytest, os
import strava_utils
import asyncio

# from async_module import AsyncClass
import asyncio
import xml_utils

STRAVA_SOURCE_CLIENT_ID = os.getenv("STRAVA_SOURCE_CLIENT_ID")
STRAVA_SOURCE_CLIENT_SECRET = os.getenv("STRAVA_SOURCE_CLIENT_SECRET")
STRAVA_SOURCE_REFRESH_TOKEN = os.getenv("STRAVA_SOURCE_REFRESH_TOKEN")

STRAVA_TARGET_CLIENT_ID = os.getenv("STRAVA_TARGET_CLIENT_ID")
STRAVA_TARGET_CLIENT_SECRET = os.getenv("STRAVA_TARGET_CLIENT_SECRET")
STRAVA_TARGET_REFRESH_TOKEN = os.getenv("STRAVA_TARGET_REFRESH_TOKEN")


@pytest.fixture
def strava_client():

    return strava_utils.get_strava_client(
        client_id=STRAVA_SOURCE_CLIENT_ID,
        client_secret=STRAVA_SOURCE_CLIENT_SECRET,
        refresh_token=STRAVA_SOURCE_REFRESH_TOKEN,
    )


@pytest.fixture
def strava_client_target():
    return strava_utils.get_strava_client(
        client_id=STRAVA_TARGET_CLIENT_ID,
        client_secret=STRAVA_TARGET_CLIENT_SECRET,
        refresh_token=STRAVA_TARGET_REFRESH_TOKEN,
    )


def test_get_strava_client(strava_client):

    assert strava_client.access_token is not None


def test_fetch_activities(strava_client):

    latest_activities = strava_utils.fetch_activities(client=strava_client, limit=1)
    print(str(latest_activities))
    activity_ids = [activity.id for activity in latest_activities]
    assert len(activity_ids) == 1


def test_fetch_activity_detail(strava_client):
    latest_activities = strava_utils.fetch_activities(client=strava_client, limit=1)

    *_, last_activity = latest_activities

    latest_activity = strava_utils.fetch_activity_detail(
        client=strava_client, activity_id=last_activity.id
    )
    print(str(latest_activity))
    assert latest_activity.average_watts != 0


@pytest.mark.asyncio
async def test_save_activity_file(strava_client):
    from datetime import datetime

    now = datetime.now()

    # Format the date and time
    formatted_date_time = now.strftime("%y%m%d%H%M%S")
    sample_output_path = f"/tmp/athlete_fit_file_{formatted_date_time}"
    latest_activities = strava_utils.fetch_activities(client=strava_client, limit=1)

    *_, last_activity = latest_activities

    await strava_utils.save_activity_file(
        client_id=STRAVA_SOURCE_CLIENT_ID,
        client_secret=STRAVA_SOURCE_CLIENT_SECRET,
        refresh_token=STRAVA_SOURCE_REFRESH_TOKEN,
        activity_id=last_activity.id,
        output_path=sample_output_path,
    )
    from pathlib import Path

    file_path = Path(
        f"{sample_output_path}.gpx"
    )  # for some reason stravagpx lib applies ext itself

    assert file_path.is_file(), f"File '{file_path}' does not exist."


@pytest.mark.asyncio
async def test_upload_activity_file(strava_client_target, strava_client):
    from datetime import datetime

    now = datetime.now()

    # Format the date and time
    formatted_date_time = now.strftime("%y%m%d%H%M%S")
    sample_output_path = f"/tmp/athlete_fit_file_{formatted_date_time}"
    latest_activities = strava_utils.fetch_activities(client=strava_client, limit=2)

    # somehow this gets the last object in an iterator
    *_, last_activity = latest_activities

    await strava_utils.save_activity_file(
        client_id=STRAVA_SOURCE_CLIENT_ID,
        client_secret=STRAVA_SOURCE_CLIENT_SECRET,
        refresh_token=STRAVA_SOURCE_REFRESH_TOKEN,
        activity_id=last_activity.id,
        output_path=sample_output_path,
    )
    from pathlib import Path

    file_path = Path(f"{sample_output_path}.gpx")

    assert file_path.is_file(), f"File '{file_path}' does not exist."
    xml_utils.move_watts_to_power(
        file_source_path=file_path, file_target_path=file_path
    )
    activity_id = strava_utils.upload_activity_file(
        strava_client_target, file_path, last_activity.name
    )

    assert activity_id is not None
    assert activity_id != 0


def test_get_refresh_token_source():
    ## TO FIX!!
    """
    Need to authorize scope
    source: https://www.strava.com/oauth/authorize?client_id=60066&response_type=code&redirect_uri=http://localhost:8085&scope=activity:read_all
    134606
    target: https://www.strava.com/oauth/authorize?client_id=134606&response_type=code&redirect_uri=http://localhost:8085&scope=activity:write,activity:read_all
    """
    auth_code = "from gui"

    # refresh_token = strava_utils.get_refresh_token_from_refresh(client_id=STRAVA_SOURCE_CLIENT_ID,
    #                           client_secret=STRAVA_SOURCE_CLIENT_SECRET,
    #                          refresh_token=STRAVA_SOURCE_REFRESH_TOKEN)

    # assert refresh_token is not None

    refresh_token = strava_utils.get_refresh_token_from_auth_code(
        client_id=STRAVA_SOURCE_CLIENT_ID,
        client_secret=STRAVA_SOURCE_CLIENT_SECRET,
        auth_code=auth_code,
    )

    assert refresh_token is not None


def test_get_refresh_token_target():
    ## TO FIX!!
    """
    Need to authorize scope
    source: https://www.strava.com/oauth/authorize?client_id=60066&response_type=code&redirect_uri=http://localhost:8085&scope=activity:read_all
    134606
    target: https://www.strava.com/oauth/authorize?client_id=134606&response_type=code&redirect_uri=http://localhost:8085&scope=activity:write,activity:read_all
    """
    auth_code = "from gui"

    # refresh_token = strava_utils.get_refresh_token_from_refresh(client_id=STRAVA_SOURCE_CLIENT_ID,
    #                           client_secret=STRAVA_SOURCE_CLIENT_SECRET,
    #                          refresh_token=STRAVA_SOURCE_REFRESH_TOKEN)

    # assert refresh_token is not None

    refresh_token = strava_utils.get_refresh_token_from_auth_code(
        client_id=STRAVA_TARGET_CLIENT_ID,
        client_secret=STRAVA_TARGET_CLIENT_SECRET,
        auth_code=auth_code,
    )

    assert refresh_token is not None


def test_get_access_token():
    refresh_token = "stored user refresh token"

    access_token = strava_utils.get_access_token(
        client_id=STRAVA_SOURCE_CLIENT_ID,
        client_secret=STRAVA_SOURCE_CLIENT_SECRET,
        refresh_token=refresh_token,
    )

    assert access_token is not None


def test_subscribe_to_strava_push(strava_client):
    STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL = os.getenv("WEBHOOK_CALLBACK_URL")
    subscription_url = "https://www.strava.com/api/v3/push_subscriptions"
    try:
        strava_utils.subscribe_to_strava_push(
            subscription_url=subscription_url,
            client_id=STRAVA_SOURCE_CLIENT_ID,
            client_secret=STRAVA_SOURCE_CLIENT_SECRET,
            callback_url=STRAVA_ACTIVITY_NOTIFICATION_CALLBACK_URL,
        )

        assert 1 == 1
    except Exception as err:
        print("test failed")
        assert 0 == 1
