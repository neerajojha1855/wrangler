import requests
from config import settings

def get_current_weather(city: str) -> dict:
    url = f"https//api.openweather.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Weather data unavailable"}
    
    data = response.json()

    return {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["main"]["speed"],
        "condition": data["weather"][0]["main"]
    }