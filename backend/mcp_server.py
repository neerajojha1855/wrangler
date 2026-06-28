from mcp.server.fastmcp import FastMCP
from services.weather import get_current_weather
from services.accommodation import get_accommodations

mcp = FastMCP("WranglerTools")

@mcp.tool()
def fetch_weather(city: str) -> str:
    data = get_current_weather(city)
    return str(data)

@mcp.tool()
def fetch_hotels(city: str, checkin: str, checkout: str) -> str:
    data = get_accommodations(city, checkin, checkout)
    return str(data)

if __name__ == "__main__":
    mcp.run()