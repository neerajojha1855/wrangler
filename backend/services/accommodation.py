import requests
from config import settings

def get_accommodations(city: str, checkin: str, checkout: str) -> list:
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
    query_string = {
        "dest_id": city,
        "search_type": "city",
        "arrival_date": checkin,
        "departure_date": checkout
    }
    
    headers = {
        "X-RapidAPI-Key": settings.RAPIDAPI_BOOKING_KEY,
        "X-RapidAPI-Host": "booking-com.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=query_string)
    if response.status_code == 200:
        return response.json().get('result', [])[:5]
    
    return []