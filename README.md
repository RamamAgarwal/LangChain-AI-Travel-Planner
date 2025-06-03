# LangChain-AI-Travel-Planner

A simple travel itinerary planner using three powerful AI agent frameworks: LangChain, CrewAI, and Pydantic AI Agents.

## Project Structure
ai-travel-planner \
├── langchain \
│   └── agent.py \
├── crewai \
│   └── crew.py \
├── pydantic_agent \
│   └── agent.py \
├── README.md  
└── requirements.txt  

## Use Case: AI Travel Planner

Our goal is to generate a travel itinerary for a user based on destination, travel dates, and preferences.

### Tools:

OpenWeather API (for weather forecast)

SerpAPI (for places to visit)

Custom PlannerTool (to assemble the itinerary)


## Conclusion

Each framework provides a unique approach to building intelligent agents:

- **LangChain**: Fast to prototype with tools

- **CrewAI**: Modular and task-specific collaboration

- **Pydantic Agents**: Strong schema validation for input/output
