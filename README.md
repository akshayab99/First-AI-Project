# AI Log Analyzer

A lightweight AI-powered application that analyzes log files and explains possible errors using a locally running language model.

This project demonstrates how modern language models can assist in understanding and interpreting system logs through a simple browser interface.

---

# Project Overview

The AI Log Analyzer allows users to:

- Ask questions using a browser interface
- Upload log files
- Receive AI-generated explanations of errors
- Understand possible root causes and suggested resolutions

The application runs entirely locally using a small language model and does not require cloud APIs.

---

# Technologies Used

- Python
- Streamlit (Web Interface)
- Ollama (Local LLM Runtime)
- TinyLlama (Language Model)
- LangChain (LLM Integration)

---

# Project Architecture

User (Browser Interface)  
↓  
Streamlit Web Application  
↓  
Python Backend  
↓  
Ollama Runtime  
↓  
TinyLlama Language Model  
↓  
AI Generated Response  

---

# Project Structure


ai-log-analyzer
│
├── app.py
├── requirements.txt
├── README.md
├── logs
   └── error.log



- app.py – main application code  
- requirements.txt – project dependencies  
- logs/ –error.log file for testing  
 

---

# Installation

## 1 Install Python

Download Python from:

https://www.python.org

Verify installation:


python --version


---

## 2 Install Ollama

Download Ollama from:

https://ollama.ai

Verify installation:


ollama --version


---

## 3 Download the TinyLlama Model

Run the following command to install the model locally:


ollama run tinyllama


This will download and install the lightweight language model.

---

## 4 Install Project Dependencies

Navigate to the project folder and run:


pip install -r requirements.txt


---

# Running the Application

Start the application using:


streamlit run app.py


Open your browser and navigate to:


http://localhost:8501


---

# Application Features

- Browser-based interface
- Upload log files for analysis
- AI-generated explanations of system errors
- Runs entirely locally without external APIs

---

# Example Log

Example log file content:

error.log content as below

2026-03-10 10:45:22 ERROR Database connection failed
java.sql.SQLTimeoutException: Connection timed out
Caused by: Network unreachable


The AI will analyze the log and provide:

- Explanation of the error
- Possible root cause
- Suggested resolution

---

# Example Use Case

1. Upload a system log file
2. Click *Analyze Log*
3. The AI reads the log and explains the issue

---

# Future Improvements

Possible enhancements include:

- Automatic detection of log formats
- Support for larger log files
- Chat-style interface with conversation history
- Integration with monitoring tools


---

# Learning Purpose

This project was built as a hands-on exercise to understand how language models can be integrated into real applications for log analysis.

It demonstrates how a local LLM can power intelligent tools without relying on external AI services.
