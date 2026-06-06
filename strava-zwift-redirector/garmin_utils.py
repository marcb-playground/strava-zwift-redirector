import os
import requests
from pathlib import Path

from strava_utils import get_access_token
from fit_utils import patch_garmin_fit_file
from garmin_client import GarminClient


def download_activity_fit(
    client_id: str,
    client_secret: str,
    refresh_token: str,
    activity_id: int,
    output_path: str,
) -> str:
    """Downloads the original Strava activity file and writes it to disk."""
    if not output_path.lower().endswith(".fit"):
        output_path = f"{output_path}.fit"

    Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
    access_token = get_access_token(client_id, client_secret, refresh_token)
    url = f"https://www.strava.com/activities/{activity_id}/export_original"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers, stream=True, verify=False)
    if response.status_code != 200:
        raise RuntimeError(
            f"Failed to download FIT file from Strava: status={response.status_code}, body={response.text}"
        )

    with open(output_path, "wb") as output_file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                output_file.write(chunk)

    return output_path


def sync_activity_to_garmin(
    source_client,
    garmin_client: GarminClient,
    activity_id: int,
    output_path: str,
    manufacturer: int = 1,
    product: int = 1836,
) -> dict:
    fit_path = download_activity_fit(
        client_id=source_client.client_id,
        client_secret=source_client.client_secret,
        refresh_token=source_client.client_refresh_token,
        activity_id=activity_id,
        output_path=output_path,
    )
    patch_garmin_fit_file(fit_path, manufacturer=manufacturer, product=product)
    return garmin_client.upload_activity_fit(fit_path, activity_name=str(activity_id))
