from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper

def langchain_travel_planner():
    search = SerpAPIWrapper()
    tools = [
        Tool(name="Search", func=search.run, description="Search for local attractions and food options")
    ]

    llm = ChatOpenAI(temperature=0)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

    query = "Plan a 3-day trip to Kyoto with local food and sightseeing."
    result = agent.run(query)
    print("LangChain Itinerary:\n", result)
