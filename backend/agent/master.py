import json
import time
from agent.spatial import plan_route

def generate_itinerary_stream(city: str, vibe: str, budget: float):
    yield f"data: {json.dumps({'status': 'INITIALIZING ENGINE...'})}\n\n"
    time.sleep(1)
    
    yield f"data: {json.dumps({'status': 'Delegating to Spatial Agent...'})}\n\n"

    final_plan = plan_route(city, vibe, budget)

    yield f"data: {json.dumps({'payload': final_plan})}\n\n"
    yield f"data: {json.dumps({'status': 'COMPLETE'})}\n\n"