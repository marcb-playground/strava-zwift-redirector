import pytest, os
import strava_utils

import asyncio
from xml_utils import move_watts_to_power
from strava_client import StravaClient
from pathlib import Path

@pytest.fixture
def strava_client_source():
    return StravaClient(client_for="source")

@pytest.fixture
def strava_client_target():
    return StravaClient(client_for="target")

def test_get_athlete(strava_client_source):
    athlete = strava_client_source.get_athlete()
    assert athlete.firstname != None

def test_get_activities(strava_client_source):
    latest_activities = strava_client_source.get_activities(limit=1)
    print(str(latest_activities))
    activity_ids = [activity.id for activity in latest_activities]
    assert len(activity_ids) == 1

@pytest.mark.asyncio
async def test_upload_activity_file(strava_client_source, strava_client_target):
    from datetime import datetime

    now = datetime.now()

    # Format the date and time
    formatted_date_time = now.strftime("%y%m%d%H%M%S")
    sample_output_path = f"/tmp/athlete_fit_file_{formatted_date_time}"
    latest_activities = strava_utils.fetch_activities(client=strava_client_source, limit=1)

    # somehow this gets the last object in an iterator
    *_, last_activity = latest_activities
    
    await strava_utils.save_activity_file(
        client_id=strava_client_source.client_id,
        client_secret=strava_client_source.client_secret,
        refresh_token=strava_client_source.client_refresh_token,
        activity_id=last_activity.id,
        output_path=sample_output_path,
    )
    

    file_path = Path(f"{sample_output_path}.gpx")

    assert file_path.is_file(), f"File '{file_path}' does not exist."
    move_watts_to_power(
        file_source_path=file_path, file_target_path=file_path
    )
    activity_id = strava_utils.upload_activity_file(
        strava_client_target, file_path, last_activity.name
    )

    assert activity_id is not None
    assert activity_id != 0

