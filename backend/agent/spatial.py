import json
from ollama import Client
from agent.budget import verify_budget
from mcp_server import fetch_weather
from config import settings

def plan_route(city: str, vibe: str, budget: float):
    # Fetch live context (e.g. Weather)
    weather = fetch_weather(city)

    # Initialize Ollama client
    client = Client(host=settings.OLLAMA_HOST)

    prompt = f"""
    You are an expert travel planner for solo backpackers.
    Plan a 1-day itinerary for {city}.
    The traveler's vibe/preference is: {vibe}.
    The current weather is: {weather}.
    Keep the total cost under {budget} INR.
    
    IMPORTANT PRICING RULE: You MUST provide highly realistic, local market prices for activities in Indian Rupees (INR). Do NOT artificially inflate prices just because the user has a high budget.

    Respond ONLY in valid JSON format following this exact structure:
    {{
      "day_1": {{
        "activities": [
          {{"name": "Activity Name", "cost": 100}}
        ]
      }}
    }}
    """

    messages = [{'role': 'user', 'content': prompt}]

    # Agent-to-Agent Negotiation Loop (Max 3 attempts)
    for attempt in range(3):
        response = client.chat(
            model=settings.OLLAMA_MODEL_NAME,
            messages=messages,
            format='json'
        )
        
        try:
            content = response['message']['content'].strip()
            # Strip markdown code blocks if the LLM adds them
            if content.startswith("```json"):
                content = content[7:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
                
            proposed_route = json.loads(content.strip())
        except Exception:
            # Tell the LLM it failed to generate JSON
            messages.append(response['message'])
            messages.append({'role': 'user', 'content': 'Your previous response was not valid JSON. You MUST output ONLY valid JSON without any markdown formatting or introductory text.'})
            continue 

        if verify_budget(proposed_route, budget):
            return proposed_route
        else:
            # Tell the LLM it failed the budget check
            messages.append(response['message'])
            messages.append({'role': 'user', 'content': f'[URGENT]: Your previous route exceeded the strict budget of {budget}. You MUST provide cheaper or free activities this time.'})

    # Absolute fallback if the AI fails 3 times
    return {
        "day_1": {"activities": [{"name": "Budget exceeded! Re-routing to a free walking tour.", "cost": 0}]}
    }