from agent import run_travel_agent

result = run_travel_agent(
    from_city="Delhi",
    to_city="Kolkata",
    num_days=3,
    budget=20000
)

print("\n" + "="*50)
print("FINAL TRAVEL PLAN")
print("="*50)
print(result)