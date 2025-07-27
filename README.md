# DeepAuto Agentic AI Engineer Technical Assignment

## 🧠 Project Overview

A multi-agent system built with LangGraph for automated Python code review and enhancement.  
This system detects bugs, suggests improvements, and generates unit tests using specialized LLM agents.

## 📦 Structure

- `agents/`: Each file defines a specialized agent (parser, bug detector, refactorer, etc.)
- `prompts/`: Prompt templates for each agent
- `tests/`: Provided test cases for evaluation
- `main.py`: Runs the LangGraph workflow
- `architecture.md`: Explains system design and agent roles
- `requirements.txt`: Python dependencies

## 🚀 How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the main workflow
python main.py
