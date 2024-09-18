import os
import stravalib
import strava_utils
class StravaClient(client_for="source"):
    client_id= None
    client_secret=None
    client_refresh_token = None

    def __init__(self,client_for):
        print(f"creating client for {client_for}")
        if client_for == "source":
            client_id = os.getenv("STRAVA_SOURCE_CLIENT_ID")
            client_secret = os.getenv("STRAVA_SOURCE_CLIENT_SECRET")
            client_refresh_token = os.getenv("STRAVA_SOURCE_REFRESH_TOKEN")

        elif client_for == "target":
            client_id = os.getenv("STRAVA_TARGET_CLIENT_ID")
            client_secret = os.getenv("STRAVA_TARGET_CLIENT_SECRET")
            client_refresh_token = os.getenv("STRAVA_TARGET_REFRESH_TOKEN")

        else:
            raise Exception("need to know for which user")

        access_token = strava_utils.get_access_token(client_id, client_secret, client_refresh_token)
        print("getting strava client")
        client = stravalib.Client(access_token=access_token)
        return client