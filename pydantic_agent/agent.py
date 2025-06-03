from pydantic import BaseModel
import openai

class TravelRequest(BaseModel):
    destination: str
    days: int
    preferences: str

class Itinerary(BaseModel):
    day1: str
    day2: str
    day3: str

def pydantic_travel_planner():
    request = TravelRequest(destination="Kyoto", days=3, preferences="local food and sightseeing")
    prompt = f"""
    Plan a 3-day itinerary for a trip to {request.destination}.
    Include {request.preferences} each day.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    print("Pydantic Itinerary:\n", response['choices'][0]['message']['content'])
