import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='API_KEY')

def get_place_details(place_id):
    place = gmaps.place(place_id)
    details = {
        'name': place['result']['name'],
        'address': place['result']['formatted_address'],
        'rating': place['result'].get('rating'),
        'reviews': place['result'].get('user_ratings_total'),
        'location': place['result']['geometry']['location'],
        'photos': [f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo['photo_reference']}&key=API_KEY"
                  for photo in place['result'].get('photos', [])[:3]]
    }
    return details