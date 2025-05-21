import gradio as gr
from dotenv import load_dotenv
from src.graph.research_graph import create_research_graph

# Load environment variables
load_dotenv()

# Create the LangGraph app
app = create_research_graph()

def ask_agent(query):
    try:
        result = app.invoke({"query": query})
        return result['answer']
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Define Gradio UI
with gr.Blocks(title="Deep Research AI Agent") as demo:
    gr.Markdown("## 🌐 Deep Research AI Assistant")
    gr.Markdown("Enter your query below and let the agents do the research!")

    query_input = gr.Textbox(label="Enter your question", placeholder="e.g. Who is the current world chess champion?")
    output_box = gr.Textbox(label="Answer", lines=10)

    submit_btn = gr.Button("Search")

    submit_btn.click(fn=ask_agent, inputs=query_input, outputs=output_box)

# Launch the app
if __name__ == "__main__":
    demo.launch()
