import json
from langchain.tools import tool

def load_flights():
    with open("data/flights.json") as f:
        return json.load(f)
    
@tool
def search_flights(from_city:str, to_city:str)-> str:
    """Search for available flights between two cities. Returns the cheapest flight option."""
    flights = load_flights()

    results= [
        f for f in flights
        if f["from"].lower() == from_city.lower()
        and f["to"].lower() == to_city.lower()
    ]

    if not results:
        return f"No Flights found from {from_city} to {to_city}"
    
    cheapest = min(results, key= lambda x: x["price"])
    fastest = min(results, key = lambda x: (
        x["arrival_time"] - x["departure_time"]
        if isinstance(x["arrival_time"], float)
        else x["arrival_time"]
    )) 

    output = f"Flights from {from_city} to {to_city}: \n"
    output += f"- Cheapest: {cheapest['airline']} | ₹{cheapest['price']} | "
    output += f"Departs: {cheapest["departure_time"]} | Arrives: {cheapest["arrival_time"]}\n"

    return output