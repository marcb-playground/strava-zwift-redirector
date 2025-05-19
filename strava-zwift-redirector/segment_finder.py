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
    # Define search parameters
    search_params = {
        'latlng': f"{latitude},{longitude}",
        'max_results': 1,
        'min_cat': 1,  # Only consider popular segments
    }
    
    try:
        # Make API request
        response = requests.get(
            'https://www.strava.com/api/v3/segments/explore',
            params=search_params,
            headers={
                'Authorization': f'Bearer {client.access_token}'
            }
        )
        response.raise_for_status()
        
        # Get the first segment from results
        segments = response.json().get('segments', [])
        if segments:
            return segments[0]
        return None
    
    except requests.RequestException as e:
        print(f"Error fetching segments: {e}")
        return None
