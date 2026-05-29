# ✈️ AI Travel Planner

An agentic AI travel planning assistant built with LangChain and Groq.

## Features
- Flight search from JSON dataset
- Hotel recommendations by city and budget
- Top tourist places discovery
- Live 7-day weather forecast
- Complete budget estimation
- Day-wise itinerary generation

## Tech Stack
- **LLM:** Groq (llama-3.3-70b-versatile)
- **Framework:** LangChain
- **UI:** Streamlit
- **Weather API:** Open-Meteo (free, no key needed)

## Live Demo
https://travel-agent-sam92769305.streamlit.app/

## Setup Locally
```bash
git clone https://github.com/YOUR_USERNAME/travel-agent
cd travel-agent
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
Add your Groq API key to `.env`:
```
GROQ_API_KEY=your_key_here
```
Run the app:
```bash
streamlit run app.py
```