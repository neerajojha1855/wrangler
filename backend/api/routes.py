from flask import Blueprint, request, Response
from agent.master import generate_itinerary_stream

api_bp = Blueprint('api', __name__)

@api_bp.route('/generate_itinerary', methods={'POST'})
def generate_itinerary():
    data = request.json
    city = data.get('city')
    vibe = data.get('vibe')
    budget = data.get('budget')

    if not all([city, vibe, budget]):
        return {"error": "Missing parameters"}, 400
        
    try:
        budget = float(budget)
    except ValueError:
        return {"error": "Invalid budget format"}, 400
    
    return Response(
        generate_itinerary_stream(city, vibe, budget),
        mimetype='text/event-stream'
    )