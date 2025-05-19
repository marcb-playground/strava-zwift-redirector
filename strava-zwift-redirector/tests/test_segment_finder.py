import pytest
from segment_finder import find_popular_segment
from strava_client import StravaClient

# Montreal's Mount Royal coordinates
MONTREAL_MOUNT_ROYAL = (45.5196, -73.5778)

@pytest.fixture
def strava_client():
    return StravaClient(client_for="source")

def test_find_popular_segment_near_montreal(strava_client):
    """
    Test finding a popular segment near Montreal's Mount Royal
    """
    segment = find_popular_segment(strava_client, *MONTREAL_MOUNT_ROYAL)
    assert segment is not None
    assert isinstance(segment, dict)
    assert 'name' in segment
    assert 'distance' in segment
    assert 'elevation_high' in segment
    assert 'elevation_low' in segment
    
    # Verify the segment is within 10km of Mount Royal
    assert segment['start_latitude'] is not None
    assert segment['start_longitude'] is not None
    
    # Calculate distance from Mount Royal
    from math import radians, cos, sin, sqrt, atan2
    
    # Convert coordinates to radians
    lat1, lon1 = radians(MONTREAL_MOUNT_ROYAL[0]), radians(MONTREAL_MOUNT_ROYAL[1])
    lat2, lon2 = radians(segment['start_latitude']), radians(segment['start_longitude'])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6371 * c  # Earth radius in kilometers
    
    assert distance <= 10  # Should be within 10km of Mount Royal
