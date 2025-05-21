import os
from langchain_groq import ChatGroq
import tiktoken

# Tokenizer for Groq (uses GPT-compatible models)
tokenizer = tiktoken.get_encoding("cl100k_base")

# Token helper
def count_tokens(text):
    return len(tokenizer.encode(text))

# Token-based chunking
def chunk_text_by_tokens(text, max_tokens=1500):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if count_tokens(" ".join(current_chunk)) > max_tokens:
            current_chunk.pop()
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# Generate summary for a chunk
def summarize_chunk(chunk, llm):
    prompt = f"Summarize this content clearly in 4–6 bullet points:\n\n{chunk}"
    return llm.predict(prompt)

# Final answer drafting agent
def draft_agent_func(state):
    research = state['research_summary']
    llm = ChatGroq(model_name="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))

    # Break into safe token chunks
    chunks = chunk_text_by_tokens(research, max_tokens=1500)

    # Summarize each chunk safely
    summaries = []
    for chunk in chunks:
        summary = summarize_chunk(chunk, llm)
        summaries.append(summary)

    final_summary = "\n".join(summaries)

    # Ensure final prompt is token-safe
    prompt_template = f"Based on the following summarized content, write a well-structured and informative answer:\n\n{final_summary}"
    if count_tokens(prompt_template) > 2000:
        final_summary = summarize_chunk(final_summary[:3000], llm)
        prompt_template = f"Based on this summarized content, write a final informative answer:\n\n{final_summary}"

    answer = llm.predict(prompt_template)
    return {"answer": answer}
