from typing import Tuple, Dict, Optional
import requests
from strava_utils import get_strava_client

def find_popular_segment(client: 'StravaClient', latitude: float, longitude: float) -> Optional[Dict]:
    """
    Find a popular segment near the given coordinates
    
    Args:
        client: StravaClient instance
        latitude: Latitude coordinate
        longitude: Longitude coordinate
        
    Returns:
        Dictionary containing segment details if found, None otherwise
    """
    # Calculate bounds for the search area (1km radius)
    lat_range = 0.009  # Approximate 1km in latitude
    lon_range = 0.014  # Approximate 1km in longitude
    
    # Create bounds parameter as [min_lat, min_lon, max_lat, max_lon]
    bounds = [
        latitude - lat_range,
        longitude - lon_range,
        latitude + lat_range,
        longitude + lon_range
    ]
    
    try:
        # Make API request
        response = requests.post(
            'https://www.strava.com/api/v3/segments/explore',
            json={
                'bounds': bounds,
                #'activity_type': 'cycling',
                #'min_cat': 1
            },
            headers={
                'Authorization': f'Bearer {client.access_token}'
            }
        )
        response.raise_for_status()
        
        # Get the first segment from results
        data = response.json()
        segments = data.get('segments', [])
        if segments and segments[0].get('effort_count', 0) > 0:
            return segments[0]
        return None
    
    except requests.RequestException as e:
        print(f"Error fetching segments: {e}")
        return None
