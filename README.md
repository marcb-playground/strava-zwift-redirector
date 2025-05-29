# strava-zwift-redirector
In order to share a Zwift account between 2 people, if the avg wattage is different enough, take from one strava and upload to another

need to authorize scopes for API cal, would do via this url

STRAVA_SOURCE_CLIENT_ID client id source
STRAVA_TARGET_CLIENT_ID client id target

    Need to authorize scope
    source: https://www.strava.com/oauth/authorize?client_id=STRAVA_SOURCE_CLIENT_ID&response_type=code&redirect_uri=http://localhost:8085&scope=activity:read_all
    STRAVA_TARGET_CLIENT_ID
    target: https://www.strava.com/oauth/authorize?client_id=STRAVA_TARGET_CLIENT_ID&response_type=code&redirect_uri=http://localhost:8085&scope=activity:write,activity:read_all
