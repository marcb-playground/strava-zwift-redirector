# strava-zwift-redirector
In order to share a Zwift account between 2 people, if the avg wattage is different enough, take from one strava and upload to another

need to authorize scopes for API cal, would do via this url

60066 client id source
134606 client id target

    Need to authorize scope
    source: https://www.strava.com/oauth/authorize?client_id=60066&response_type=code&redirect_uri=http://localhost:8085&scope=activity:read_all
    134606
    target: https://www.strava.com/oauth/authorize?client_id=134606&response_type=code&redirect_uri=http://localhost:8085&scope=activity:write,activity:read_all
