# AI Log Analyzer

A lightweight AI-powered application that analyzes log files and explains possible errors using a local language model.

## Overview

This project demonstrates how modern language models can be used to simplify log analysis.

The application allows users to:

- Ask questions through a simple web interface
- Upload log files
- Receive AI-generated explanations of possible errors and causes

The system runs entirely locally using a small language model.

## Tech Stack

- Python
- Streamlit (UI)
- Ollama (Local LLM runtime)
- TinyLlama (Language Model)

## Architecture

User Interface → Python Application → Ollama → TinyLlama → AI Response

## Features

- Local AI-powered log analysis
- Browser-based interface
- File upload for log analysis
- AI-generated explanation of system errors

## Installation

1. Install Python
2. Install Ollama
3. Download the TinyLlama model
