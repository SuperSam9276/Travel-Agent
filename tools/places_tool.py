import json 
from langchain.tools import tool

def load_places():
    with open('data/places.json') as f:
        return json.load(f)
    
@tool
def search_places(city: str) -> list:
    """Find top tourist attractions and places to visit in a city. Returns top 5 places by rating."""
    places= load_places()

    results= [
        p for p in places
        if p['city'].lower() == city.lower()
    ]

    if not results:
        return f"No placecs found in {city}"
    
    top = sorted(results, key=lambda x: x['rating'], reverse = True)[:5]

    output = f"Top places in {city}:\n"

    for p in top:
        output += f"{p['name']} | Type:{p['type']} | Rating: {p['rating']}⭐\n"

    return output