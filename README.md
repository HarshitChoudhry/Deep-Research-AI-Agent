# 🧠 Deep Research AI Agent

The **Deep Research AI Agent** is an intelligent assistant that combines real-time web search with advanced language generation to provide users with accurate, well-structured answers to complex questions. It uses Tavily for online research and Groq's LLaMA 3 model to generate human-like responses.

---

## 🔍 How It Works

1. **User Input:** You enter a research query via a simple Gradio web interface.
2. **Research Agent:** The query is passed to an agent that uses the Tavily API to conduct detailed real-time web research.
3. **Drafting Agent:** The research findings are forwarded to a drafting agent powered by Groq’s LLaMA 3.1 (8B), which generates a clean, concise, and informative response.
4. **Final Output:** The final answer is displayed in the Gradio interface for the user.

This modular architecture is powered by LangGraph, which coordinates the workflow between the agents seamlessly.

---

## 💻 How to Run

### 1. Clone and Setup Environment

git clone https://github.com/HarshitChoudhry/Deep-Research-AI-Agent.git
cd Deep-Research-AI-Agent
python -m venv myenv
myenv\Scripts\activate 
pip install -r requirements.txt 

### 2. Set Up Environment Variables

Create a .env file in the root directory and add your API keys:

GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

### 3. Run the Web Interface

python app.py

## 🛠️ Tech Stack

- **LangChain** – Framework for building agentic LLM applications
- **LangGraph** – State graph management for coordinating agents
- **Groq API** – Ultra-fast inference with LLaMA 3.1 (8B) for answer generation
- **Tavily**  – Real-time web search for up-to-date research data
- **Gradio**  – User-friendly UI for interaction


