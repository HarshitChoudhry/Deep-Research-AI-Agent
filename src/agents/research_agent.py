from langchain.agents import Tool, initialize_agent
from langchain.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
import os

llm = ChatGroq(model_name="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))
tavily_tool = TavilySearchResults(k=3)

tools = [
    Tool(
        name="Tavily",
        func=tavily_tool.run,
        description="Conducts online research using Tavily."
    )
]

def research_agent_func(state):
    query = state['query']
    agent = initialize_agent(tools, llm, agent="chat-zero-shot-react-description")
    research_output = agent.run(f"Do detailed web research on: {query} and extract useful information.")
    return {"research_summary": research_output}
