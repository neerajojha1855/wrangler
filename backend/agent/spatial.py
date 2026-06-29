import json
from ollama import Client
from agent.budget import verify_budget
from mcp_server import fetch_weather
from config import settings

def plan_route(city: str, days: int, vibe: str, budget: float):
    # Fetch live context (e.g. Weather)
    weather = fetch_weather(city)

    # Initialize Ollama client
    client = Client(host=settings.OLLAMA_HOST)

    prompt = f"""
    You are an expert travel planner for solo backpackers.
    Plan a itinerary for {city}.
    The trip is for {days} days.
    The traveler's vibe/preference is: {vibe}.
    The current weather is: {weather}.
    Keep the total cost under {budget}.

    Respond ONLY in valid JSON format following this exact structure:
    {{
      "day_1": {{
        "activities": [
          {{"name": "Activity Name", "cost": 100}}
        ]
      }}
    }}
    """

    # Agent-to-Agent Negotiation Loop (Max 3 attempts)
    for attempt in range(3):
        response = client.chat(
            model=settings.OLLAMA_MODEL_NAME,
            messages=[{'role': 'user', 'content': prompt}],
            format='json'
        )
        
        try:
            proposed_route = json.loads(response['message']['content'])
        except Exception:
            continue # If it outputs bad JSON, just try again
    proposed_route = {
        "day_1": {"activities": [{"name": "Fort Visit", "cost": 20}]},
        "day_2": {"activities": [{"name": "Local Market Shopping", "cost": 400}]}
    }

        if verify_budget(proposed_route, budget):
            return proposed_route
        else:
            # Agent feedback loop: update the prompt to enforce the constraint harder
            prompt += f"\n\n[URGENT]: Your previous route exceeded the strict budget of {budget}. You MUST provide cheaper or free activities this time."

    # Absolute fallback if the AI fails 3 times
    return {
        "day_1": {"activities": [{"name": "Budget exceeded! Re-routing to a free walking tour.", "cost": 0}]}
    }
