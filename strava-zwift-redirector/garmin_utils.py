import asyncio
import shutil
import time
from pathlib import Path

from config import settings as app_settings
from fit_utils import patch_garmin_fit_file
from strava_utils import download_activity_fit, save_activity_file
from garmin_client import GarminClient
from xml_utils import move_watts_to_power

GPX_ACTIVITY_TYPE_MAP = {
    "virtualride": "Ride",
    "virtual_ride": "Ride",
    "virtualrun": "Run",
    "virtual_run": "Run",
    "ebikeride": "Ride",
    "indoorride": "Ride",
    "indoor_ride": "Ride",
    "indoorrun": "Run",
    "indoor_run": "Run",
    "ride": "Ride",
    "run": "Run",
    "walk": "Walk",
    "hike": "Hike",
    "other": "Other",
}


def _normalize_gpx_activity_type(file_path: str, activity_type: str | None = None) -> None:
    if not file_path.lower().endswith(".gpx"):
        return

    try:
        content = Path(file_path).read_text(encoding="utf-8")
    except Exception:
        return

    normalized = None
    if activity_type:
        normalized = GPX_ACTIVITY_TYPE_MAP.get(str(activity_type).strip().lower(), None)
    if normalized is None:
        activity_type_value = str(activity_type).strip().lower() if activity_type is not None else None
        if activity_type_value:
            for src, dst in GPX_ACTIVITY_TYPE_MAP.items():
                if src in activity_type_value:
                    normalized = dst
                    break
    if normalized is None:
        for src, dst in GPX_ACTIVITY_TYPE_MAP.items():
            if f"<type>{src}</type>" in content:
                normalized = dst
                break

    if normalized and f"<type>{normalized}</type>" not in content:
        for src, dst in GPX_ACTIVITY_TYPE_MAP.items():
            content = content.replace(f"<type>{src}</type>", f"<type>{dst}</type>")
        try:
            Path(file_path).write_text(content, encoding="utf-8")
        except Exception:
            pass


def sync_activity_to_garmin(
    source_client,
    garmin_client: GarminClient,
    activity_id: int,
    output_path: str,
    activity_name: str | None = None,
    manufacturer: int | None = None,
    product: int | None = None,
    activity_type: str | None = None,
    require_fit: bool = False,
) -> dict:
    if manufacturer is None:
        manufacturer = getattr(app_settings, "GARMIN_MANUFACTURER", 1)
    if product is None:
        product = getattr(app_settings, "GARMIN_PRODUCT", 1836)

    if activity_type is None:
        try:
            src_act = source_client.stravalib_client.get_activity(activity_id)
            activity_type = getattr(src_act, "type", None) or getattr(src_act, "sport_type", None)
            if activity_type is not None:
                # Handle enum objects by extracting .value, otherwise convert to string
                activity_type = getattr(activity_type, "value", str(activity_type)).strip()
        except Exception:
            activity_type = None
    else:
        # Handle enum objects by extracting .value, otherwise convert to string
        activity_type = getattr(activity_type, "value", str(activity_type)).strip()

    activity_file_path = None
    was_fit = False

    try:
        activity_file_path = download_activity_fit(
            client_id=source_client.client_id,
            client_secret=source_client.client_secret,
            refresh_token=source_client.client_refresh_token,
            activity_id=activity_id,
            output_path=output_path,
        )
        was_fit = True
    except RuntimeError as e:
        if require_fit:
            raise RuntimeError(f"FIT file required but download failed for activity {activity_id}: {str(e)}") from e

        base = output_path
        if base.lower().endswith(".fit"):
            base = base[:-4]
        if base.lower().endswith(".gpx"):
            base = base[:-4]

        activity_file_path = asyncio.run(
            save_activity_file(
                client_id=source_client.client_id,
                client_secret=source_client.client_secret,
                refresh_token=source_client.client_refresh_token,
                activity_id=activity_id,
                output_path=base,
            )
        )

        candidates = [
            activity_file_path,
            f"{activity_file_path}.gpx",
            f"{base}.gpx",
        ]
        found = None
        for c in candidates:
            if Path(c).is_file():
                found = c
                break
        if found is None:
            raise RuntimeError(f"Could not locate GPX file after export; checked: {candidates}")
        activity_file_path = found
        was_fit = False

    try:
        data_dir = Path(__file__).resolve().parent / "tests" / "data"
        if data_dir.is_dir() and activity_file_path:
            timestamp = int(time.time())
            raw_copy = data_dir / f"input_{activity_id}_{timestamp}{Path(activity_file_path).suffix}"
            shutil.copy(activity_file_path, raw_copy)
    except Exception:
        pass

    if was_fit:
        patch_garmin_fit_file(activity_file_path, manufacturer=manufacturer, product=product)
    else:
        _normalize_gpx_activity_type(activity_file_path, activity_type)
        try:
            move_watts_to_power(activity_file_path, activity_file_path)
        except Exception:
            pass

    try:
        data_dir = Path(__file__).resolve().parent / "tests" / "data"
        if data_dir.is_dir() and activity_file_path:
            timestamp = int(time.time())
            out_copy = data_dir / f"output_{activity_id}_{timestamp}{Path(activity_file_path).suffix}"
            shutil.copy(activity_file_path, out_copy)
    except Exception:
        pass

    upload_result = garmin_client.upload_activity_fit(
        activity_file_path,
        activity_name=activity_name or str(activity_id),
    )

    return {
        "result": upload_result,
        "file_path": activity_file_path,
    }
