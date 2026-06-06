import asyncio
from pathlib import Path

from strava_utils import download_activity_fit, save_activity_file
from fit_utils import patch_garmin_fit_file, read_fit_file_id_values
from config import settings as app_settings
import shutil
import time
from garmin_client import GarminClient
from xml_utils import move_watts_to_power


def sync_activity_to_garmin(
    source_client,
    garmin_client: GarminClient,
    activity_id: int,
    output_path: str,
    activity_name: str | None = None,
    manufacturer: int | None = None,
    product: int | None = None,
) -> dict:
    # Use shared config defaults when explicit values are not provided
    if manufacturer is None:
        manufacturer = getattr(app_settings, "GARMIN_MANUFACTURER", 1)
    if product is None:
        product = getattr(app_settings, "GARMIN_PRODUCT", 1836)

    try:
        activity_file_path = download_activity_fit(
            client_id=source_client.client_id,
            client_secret=source_client.client_secret,
            refresh_token=source_client.client_refresh_token,
            activity_id=activity_id,
            output_path=output_path,
        )
        # If tests/data exists in repo, save a copy of the raw downloaded file
        try:
            data_dir = Path(__file__).resolve().parent / "tests" / "data"
            if data_dir.is_dir():
                timestamp = int(time.time())
                raw_copy = data_dir / f"input_{activity_id}_{timestamp}{Path(activity_file_path).suffix}"
                shutil.copy(activity_file_path, raw_copy)
        except Exception:
            pass
        patch_garmin_fit_file(activity_file_path, manufacturer=manufacturer, product=product)
        # Save patched/uploaded copy if tests/data exists
        try:
            data_dir = Path(__file__).resolve().parent / "tests" / "data"
            if data_dir.is_dir():
                timestamp = int(time.time())
                out_copy = data_dir / f"output_{activity_id}_{timestamp}{Path(activity_file_path).suffix}"
                shutil.copy(activity_file_path, out_copy)
        except Exception:
            pass
    except RuntimeError as err:
        # Strava FIT export is not always available from the API; fallback to GPX export.
        # strava2gpx may append a .gpx extension even if provided. Pass a
        # base path (without .gpx) and then locate the actual created file.
        base = output_path
        if base.lower().endswith(".fit"):
            base = base[:-4]
        if base.lower().endswith(".gpx"):
            base = base[:-4]

        created = asyncio.run(
            save_activity_file(
                client_id=source_client.client_id,
                client_secret=source_client.client_secret,
                refresh_token=source_client.client_refresh_token,
                activity_id=activity_id,
                output_path=base,
            )
        )

        # Try common candidate filenames the exporter might have created.
        candidates = [
            created,
            f"{created}.gpx",
            f"{created}.gpx.gpx",
            f"{base}.gpx",
            f"{base}.gpx.gpx",
        ]
        activity_file_path = None
        for c in candidates:
            if Path(c).is_file():
                activity_file_path = c
                break

        if activity_file_path is None:
            raise RuntimeError(f"Could not locate GPX file after export; checked: {candidates}")

        move_watts_to_power(activity_file_path, activity_file_path)

    upload_result = garmin_client.upload_activity_fit(
        activity_file_path,
        activity_name=activity_name or str(activity_id),
    )
    # Try to set the activity type in Garmin so Training Load is computed.
    try:
        # Determine source activity sport (e.g., 'Ride', 'Run')
        sport = None
        try:
            src_act = source_client.stravalib_client.get_activity(activity_id)
            sport = getattr(src_act, "type", None) or getattr(src_act, "sport_type", None)
            if sport:
                sport = str(sport).lower()
        except Exception:
            sport = None

        client = garmin_client._create_client()
        try:
            client.login()
        except Exception:
            pass

        # Fetch available activity types from Garmin and choose a match
        try:
            types = client.get_activity_types()
            chosen = None
            if isinstance(types, list):
                for t in types:
                    key = str(t.get("typeKey", "")).lower()
                    name = str(t.get("name", "")).lower()
                    if sport and (sport in key or sport in name):
                        chosen = t
                        break
            elif isinstance(types, dict):
                # some implementations return dict of lists
                for v in types.values():
                    if not isinstance(v, list):
                        continue
                    for t in v:
                        key = str(t.get("typeKey", "")).lower()
                        name = str(t.get("name", "")).lower()
                        if sport and (sport in key or sport in name):
                            chosen = t
                            break
                    if chosen:
                        break

            if chosen:
                # Find the most recent activity id (assume it's the one we uploaded)
                last = client.get_last_activity()
                if last and isinstance(last, dict):
                    activity_id_garmin = last.get("activityId") or last.get("activityIdLocal") or last.get("activity_id") or last.get("id")
                    if activity_id_garmin:
                        try:
                            client.set_activity_type(
                                str(activity_id_garmin),
                                int(chosen.get("typeId")),
                                str(chosen.get("typeKey")),
                                int(chosen.get("parentTypeId") or 0),
                            )
                        except Exception:
                            pass
        except Exception:
            pass
    except Exception:
        # never raise from activity-type patching
        pass

    return {
        "result": upload_result,
        "file_path": activity_file_path,
    }
