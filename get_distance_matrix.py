import requests

def get_distance_matrix(api_key, origins, destinations, mode='driving'):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    
    params = {
        'origins': '|'.join(origins),
        'destinations': '|'.join(destinations),
        'mode': mode,
        'key': api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        return data['rows']
    else:
        return None