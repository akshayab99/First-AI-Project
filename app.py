import streamlit as st
from langchain_community.llms import Ollama

# connect to TinyLlama running locally
llm = Ollama(model="tinyllama")

st.set_page_config(page_title="Akshay Bandal's AI Agent")

st.title("AB's AI Agent")

st.write("Ask questions or upload logs to analyze errors.")

# ---------- Ask Question Section ----------

st.header("How may I help you?")

question = st.text_input("Enter your question")

if st.button("Get Answer"):

    if question:
        prompt = f"""
You are a expert. Answer the following question clearly:

Question:
{question}
"""
        response = llm.invoke(prompt)

        st.subheader("AI Response")
        st.write(response)

# ---------- Log Analysis Section ----------

st.header("Upload Logs to Analyze")

uploaded_file = st.file_uploader("Upload a log file", type=["log","txt"])

if uploaded_file is not None:

    log_content = uploaded_file.read().decode("utf-8")

    if st.button("Analyze Logs"):

        prompt = f"""
You are a troubleshooting expert.

Analyze the following log file and explain:

1. What the error is
2. Possible root cause
3. Suggested fix

Log:
{log_content}
"""

        analysis = llm.invoke(prompt)

        st.subheader("Log Analysis Result")
        st.write(analysis)
