from langchain.tools import tool

@tool
def estimate_budget(flight_price: int, hotel_price_per_night: int, num_days: int) -> str:
    """Estimate total trip budget based on flight price, hotel price per night, and number of days."""
    hotel_total = hotel_price_per_night * num_days
    daily_expenses = 1500 * num_days  # avg food + local travel per day
    total = flight_price + hotel_total + daily_expenses

    return (
        f"Budget Breakdown:\n"
        f"- Flight:           ₹{flight_price}\n"
        f"- Hotel ({num_days} nights): ₹{hotel_total}\n"
        f"- Food & Travel:    ₹{daily_expenses}\n"
        f"------------------------------\n"
        f"- Total Estimated:  ₹{total}"
    )