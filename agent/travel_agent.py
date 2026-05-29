from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools.flight_tool import search_flights
from tools.hotel_tool import search_hotels
from tools.places_tool import search_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget
import re

load_dotenv()

def run_travel_agent(from_city: str, to_city: str, num_days: int, budget: int) -> str:
    """Run the travel agent with explicitly provided cities."""

    # Step 1: Call all tools directly in Python — no LLM involvement
    flights_result = search_flights.invoke({"from_city": from_city, "to_city": to_city})
    hotels_result = search_hotels.invoke({"city": to_city, "max_price": budget // num_days})
    places_result = search_places.invoke({"city": to_city})
    weather_result = get_weather.invoke({"city": to_city})

    # Extract flight price for budget estimation
    price_match = re.search(r'₹(\d+)', flights_result)
    flight_price = int(price_match.group(1)) if price_match else 0

    # Extract hotel price for budget estimation
    hotel_match = re.search(r'₹(\d+)/night', hotels_result)
    hotel_price = int(hotel_match.group(1)) if hotel_match else 2000

    budget_result = estimate_budget.invoke({
        "flight_price": flight_price,
        "hotel_price_per_night": hotel_price,
        "num_days": num_days
    })

    # Step 2: Pass all results to LLM only for formatting
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

    prompt = f"""You are a travel assistant. Format this data into a beautiful travel plan.

TRIP: {from_city} → {to_city} | {num_days} days | Budget: ₹{budget}

FLIGHTS DATA:
{flights_result}

HOTELS DATA:
{hotels_result}

PLACES DATA:
{places_result}

WEATHER DATA:
{weather_result}

BUDGET DATA:
{budget_result}

Write a complete travel plan with these sections:
✈️ Flight Details
🏨 Hotel Recommendation
📍 Day-wise Itinerary (use the places listed above, spread across {num_days} days)
🌤️ Weather Summary
💰 Budget Breakdown"""

    response = llm.invoke(prompt)
    return response.content