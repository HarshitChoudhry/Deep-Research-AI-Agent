import os
from src.graph.research_graph import create_research_graph
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Entry point: Get user query and start the research process
if __name__ == "__main__":
    user_query = input("Enter your research query: ")

    # Create and run the research graph
    app = create_research_graph()
    result = app.invoke({"query": user_query})

    print("\n--- FINAL ANSWER ---\n")
    print(result['answer'])
