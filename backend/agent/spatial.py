from agent.budget import verify_budget
from mcp_server import fetch_weather

def plan_route(city: str, days: int, vibe: str, budget: float):
    weather = fetch_weather(city)

    proposed_route = {
        "day_1": {"activities": [{"name": "Fort Visit", "cost": 20}]},
        "day_2": {"activities": [{"name": "Local Market Shopping", "cost": 400}]}
    }

    if verify_budget(proposed_route, budget):
        return proposed_route
    else:
        return {
            "day_1": {"activities": [{"name": "Free Walking Tour", "cost": 0}]}
        }