import os
import streamlit as st
from agent.travel_agent import run_travel_agent


# --- Page Config ---
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="centered"
)

# --- Header ---
st.title("✈️ AI Travel Planner")
st.markdown("Plan your perfect India trip powered by AI")
st.divider()

# --- Input Form ---
col1, col2 = st.columns(2)

CITIES = [
    "Bangalore", "Chennai", "Delhi",
    "Goa", "Hyderabad", "Jaipur",
    "Kolkata", "Mumbai", "Pune", "Ahmedabad"
]

with col1:
    from_city = st.selectbox("🛫 From", CITIES, index=2)
    num_days = st.slider("🗓️ Number of Days", min_value=1, max_value=7, value=3)

with col2:
    to_city = st.selectbox("🛬 To", CITIES, index=4)
    budget = st.number_input("💰 Budget (₹)", min_value=5000, max_value=200000,
                              value=20000, step=1000)

st.divider()

# --- Generate Button ---
if st.button("🗺️ Generate Travel Plan", use_container_width=True, type="primary"):
    if from_city == to_city:
        st.error("Source and destination cities cannot be the same!")
    else:
        with st.spinner("Planning your trip... This may take a few seconds ✈️"):
            result = run_travel_agent(
                from_city=from_city,
                to_city=to_city,
                num_days=num_days,
                budget=budget
            )

        st.success("Your travel plan is ready!")
        st.divider()
        st.markdown(result)