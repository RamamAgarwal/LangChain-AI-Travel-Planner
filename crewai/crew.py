from crewai import Crew, Agent, Task
from langchain.chat_models import ChatOpenAI

def crewai_travel_planner():
    llm = ChatOpenAI()

    researcher = Agent("Researcher", llm)
    planner = Agent("Planner", llm)

    task1 = Task("Find top tourist spots and food joints in Kyoto.", researcher)
    task2 = Task("Create a 3-day itinerary using results from Task 1.", planner, depends_on=[task1])

    crew = Crew([task1, task2])
    crew.kickoff()
