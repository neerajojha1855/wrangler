# Wrangler - Autonomous Travel Logistics Agent

Wrangler is an AI-powered travel logistics agent that crafts hyper-optimized, budget-conscious vacation blueprints tailored to your specific "vibe". Built with a striking Neo-Brutalist frontend and powered by a multi-agent backend using Ollama, Wrangler automates the complex task of itinerary planning.

## Features
- **Multi-Agent Orchestration:** Utilizes a Master Agent alongside Spatial and Budget sub-agents to negotiate and generate a logical, affordable itinerary.
- **Neo-Brutalist UI:** A fast, responsive frontend designed with bold colors, hard borders, and flat shadows.
- **FastAPI Backend:** A lightweight, asynchronous Python API.
- **MCP Integration:** Leverages the Model Context Protocol (MCP) to pull in contextual data like historical weather and POIs.

## Tech Stack
- **Frontend:** HTML, Vanilla JS, Tailwind CSS
- **Backend:** FastAPI, Uvicorn, Pydantic
- **AI SDKs:** Ollama, MCP (FastMCP)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/neerajojha1855/wrangler.git
   cd wrangler
   ```

2. **Create a virtual environment & install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Context Server and the API:**
   Ensure Ollama is running locally, then start your FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```

## Usage
Open `http://127.0.0.1:8000` (or your configured frontend host) in your browser. Enter your destination, budget, and vibe, then hit `[!] GENERATE` to watch the agent swarm coordinate your itinerary in real-time.
