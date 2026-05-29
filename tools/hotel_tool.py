import json
from langchain.tools import tool

def load_hotels():
    with open("data/hotels.json") as f:
        return json.load(f)
    
@tool
def search_hotels(city: str, max_price: int= 10000) -> str:
    """Search for hotels in a city within a budget. Returns top 3 hotels sorted by star rating."""
    hotels = load_hotels()

    results = [
        h for h in hotels
        if h["city"].lower() == city.lower()
        and h["price_per_night"] <= max_price
    ]

    if not results:
        return  f"No hotel found in {city} under ₹{max_price}/night"
    
    top = sorted(results, key=lambda x: x["stars"], reverse=True)[:3]

    output = f"Top hotels in {city}:\n"
    for h in top:
        output += f"- {h['name']} | {h['stars']}⭐ | ₹{h['price_per_night']}/night | Amenities: {', '.join(h['amenities'])}\n"

    return output