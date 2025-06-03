from langchain.agent import langchain_travel_planner
from crewai.crew import crewai_travel_planner
from pydantic_agent.agent import pydantic_travel_planner

if __name__ == "__main__":
    print("=== LangChain ===")
    langchain_travel_planner()

    print("\n=== CrewAI ===")
    crewai_travel_planner()

    print("\n=== Pydantic AI Agent ===")
    pydantic_travel_planner()
