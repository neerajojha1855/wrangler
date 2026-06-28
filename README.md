# Wrangler - Autonomous Travel Logistics Agent

Wrangler is an AI-powered, offline-first travel logistics agent that crafts hyper-optimized, budget-conscious vacation blueprints tailored to your specific "vibe". Built with a striking Neo-Brutalist frontend and powered by a multi-agent backend using Ollama, Wrangler automates the complex task of itinerary planning while protecting your privacy through local inference.

## Features
- **Multi-Agent Orchestration:** Utilizes a Master Agent alongside Spatial and Budget sub-agents to negotiate and generate a logical, affordable itinerary.
- **Offline-First Resilience:** Progressive Web App (PWA) architecture caches maps and data for use in remote areas without cell service.
- **Neo-Brutalist UI:** A fast, responsive frontend designed with bold colors, hard borders, and flat shadows, optimized for low battery usage and outdoor visibility.
- **Flask Backend:** A lightweight Python API serving as the gateway between the UI and local AI models.
- **Accurate SOS Protocol:** Generates emergency plans using verified data sources cross-referenced with contextual LLM survival advice.
- **Dynamic Packing Matrix:** Generates biome-aware packing lists exportable as PDFs.

## Tech Stack
- **Frontend:** Vanilla HTML/JS, Tailwind CSS, Leaflet.js, Vite
- **Backend:** Flask, SQLite
- **AI Engine:** Ollama (Qwen3.5), FastMCP

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/neerajojha1855/wrangler.git
   cd wrangler
   ```

2. **Backend Setup:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
   *Note: Ensure your `.env` file is properly configured with your API keys (use `.env.example` as a template).*

3. **Frontend Setup (Vite):**
   *(Assuming Node.js is installed)*
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Run the Context Server and the API:**
   Ensure Ollama is running locally, then start your Flask backend:
   ```bash
   python main.py
   ```

## Usage
Open the provided Vite dev server URL (e.g., `http://localhost:5173`) in your browser. Enter your destination, budget, and vibe, then hit the generate button to watch the agent swarm coordinate your itinerary in real-time.

## Contributing
Please see `CONTRIBUTE.md` for guidelines on how to contribute to Wrangler.
