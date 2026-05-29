import requests
from langchain.tools import tool

CITY_COORD = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "goa": (15.2993, 74.1240),
    "bangalore": (12.9716, 77.5946),
    "hyderabad": (17.3850, 78.4867),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "jaipur": (26.9124, 75.7873),
    "pune": (18.5204, 73.8567),
    "ahmedabad": (23.0225, 72.5714)
}

@tool
def get_weather(city: str) -> str:
    """Get 7-day weather forecast for a city. Returns daily max/min temperatures and rainfall."""
    coords = CITY_COORD.get(city.lower())

    if not coords: 
        return f"Sorry, I don't have weather data for {city}."
    
    lat, lon = coords
    url = "https://api.open-meteo.com/v1/forecast"

    params = [
        ("latitude", lat),
        ("longitude", lon),
        ("daily", "temperature_2m_max"),
        ("daily", "temperature_2m_min"),
        ("daily", "precipitation_sum"),
        ("daily", "weather_code"),
        ("timezone", "auto"),
        ("forecast_days", 7)
    ]

    try:
        response = requests.get(url, params= params)
        data = response.json()
        daily = data["daily"]

        output = f"7-Day Weather Forecast for {city.title()}:\n"
        for i in range(7):
            output += (
                f"{daily['time'][i]}:"
                f"Max Temp: {daily['temperature_2m_max'][i]}°C |"
                f"Min Temp: {daily['temperature_2m_min'][i]}°C |"
                f"Rain: {daily['precipitation_sum'][i]}mm |"
            )
        return output
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"