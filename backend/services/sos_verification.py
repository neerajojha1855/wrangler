import requests

def get_nearest_hospitals(lat: float, lon: float, radius: int=5000) -> list:
    overpass_url = "https://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    node["amenity"="hospital"](around:{radius},{lat},{lon});
    out 3;
    """

    response = requests.get(overpass_url, params={'data': overpass_query})
    if response.status_code == 200:
        elements = response.json().get("elements", [])
        return [{"name": el.get("tags", {}).get("name", "unknown hospital"), "lat": el["lat"], "lon": el["lon"]} for el in elements]
    
    return []