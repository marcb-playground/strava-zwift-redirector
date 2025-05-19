import os
import stravalib
from strava_utils import get_access_token


class StravaClient:
    client_id = None
    client_secret = None
    client_refresh_token = None
    stravalib_client = None
    access_token = None

    def __init__(self, client_for):
        print(f"creating client for {client_for}")
        if client_for == "source":
            self.client_id = os.getenv("STRAVA_SOURCE_CLIENT_ID")
            self.client_secret = os.getenv("STRAVA_SOURCE_CLIENT_SECRET")
            self.client_refresh_token = os.getenv("STRAVA_SOURCE_REFRESH_TOKEN")
            print("source info")

        elif client_for == "target":
            self.client_id = os.getenv("STRAVA_TARGET_CLIENT_ID")
            print(f" target client id: {self.client_id}")
            self.client_secret = os.getenv("STRAVA_TARGET_CLIENT_SECRET")
            print(self.client_secret)
            self.client_refresh_token = os.getenv("STRAVA_TARGET_REFRESH_TOKEN")
            print("target info")
        else:
            raise Exception("need to know for which user")
        self.access_token = get_access_token(
            self.client_id, self.client_secret, self.client_refresh_token
        )

        print("getting strava client")
        self.stravalib_client = stravalib.Client(access_token=self.access_token)
        print(f"got stravalib client")

    def get_athlete(self, athlete_id=None):

        athlete = self.stravalib_client.get_athlete(athlete_id=athlete_id)

        return athlete

    def get_activities(self, limit=1):
        activities = self.stravalib_client.get_activities(limit=limit)
        return activities
