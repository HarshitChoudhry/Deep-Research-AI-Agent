from langgraph.graph import StateGraph
from typing import TypedDict, Annotated
from src.agents.research_agent import research_agent_func
from src.agents.draft_agent import draft_agent_func

class AgentState(TypedDict):
    query: str
    research_summary: Annotated[str, "Research Summary"]
    answer: Annotated[str, "Final Answer"]

def create_research_graph():
    graph = StateGraph(AgentState)
    graph.add_node("do_research", research_agent_func)
    graph.add_node("draft_response", draft_agent_func)
    graph.add_node("end", lambda state: state)

    graph.set_entry_point("do_research")
    graph.add_edge("do_research", "draft_response")
    graph.add_edge("draft_response", "end")

    return graph.compile()
