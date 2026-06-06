import os
from pathlib import Path

import pytest

from garmin_client import GarminClient
from garmin_utils import sync_activity_to_garmin
from strava_client import StravaClient
from config import settings as app_settings
from fit_utils import read_fit_file_id_values


INTEGRATION_ENV_VARS = [
    "STRAVA_SOURCE_CLIENT_ID",
    "STRAVA_SOURCE_CLIENT_SECRET",
    "STRAVA_SOURCE_REFRESH_TOKEN",
    "GARMIN_CONNECT_USERNAME",
    "GARMIN_CONNECT_PASSWORD",
]


def _integration_env_vars_present():
    return [name for name in INTEGRATION_ENV_VARS if not os.getenv(name)]


@pytest.mark.integration
def test_sync_latest_strava_activity_to_garmin(tmp_path: Path):
    missing = _integration_env_vars_present()
    if missing:
        pytest.skip(f"Integration credentials required: {', '.join(missing)}")

    source_client = StravaClient("source")
    activities = source_client.get_activities(limit=1)
    latest_activity = None

    if hasattr(activities, "__iter__"):
        try:
            latest_activity = next(iter(activities))
        except StopIteration:
            latest_activity = None
    else:
        latest_activity = activities

    assert latest_activity is not None, "No source Strava activities are available"
    activity_id = getattr(latest_activity, "id", None) or getattr(latest_activity, "activity_id", None)
    assert activity_id is not None, "Could not determine latest Strava activity ID"

    output_path = str(tmp_path / f"strava_activity_{activity_id}.fit")
    garmin_client = GarminClient()

    # instruct the shared config to use a non-default manufacturer/product
    app_settings.GARMIN_MANUFACTURER = 99
    app_settings.GARMIN_PRODUCT = 100

    result = sync_activity_to_garmin(
        source_client=source_client,
        garmin_client=garmin_client,
        activity_id=activity_id,
        output_path=output_path,
    )

    assert isinstance(result, dict)
    assert result.get("result") is not None
    assert result.get("file_path") is not None
    assert Path(result["file_path"]).is_file()
    # If we ended up with a FIT file, verify the patched manufacturer/product
    fp = Path(result["file_path"])
    if fp.suffix.lower() == ".fit":
        vals = read_fit_file_id_values(str(fp))
        assert vals.get(1) == 99
        assert vals.get(2) == 100
