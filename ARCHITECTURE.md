# Wrangler Architecture

Wrangler is an autonomous travel logistics agent designed to create hyper-optimized vacation blueprints based on user vibe and budget constraints. The system consists of three main layers:

## High-Level System Flow

```mermaid
flowchart TD
    User([User]) -->|Input Constraints: Vibe, Budget, Dest| UI[Frontend: Neo-Brutalist UI]
    UI -->|Async POST /api/generate_itinerary| API[Backend: FastAPI Gateway]
    
    API -->|Dispatch Task| Orchestrator[Master Agent / Ollama]
    
    subgraph Agent Swarm
        Orchestrator -->|Delegates Spatial routing| Spatial[Spatial Sub-Agent]
        Spatial -->|Proposes Route| Budget[Budget Sub-Agent]
        Budget -->|Rejects/Approves| Spatial
    end
    
    subgraph FastMCP Context Server
        Spatial <-->|Fetch POIs & Weather| MCP[FastMCP Tools]
    end
    
    Budget -->|Final Approved Itinerary| Orchestrator
    Orchestrator -->|Returns JSON Payload| API
    API -->|Sends Data| UI
    UI -->|Renders Matrix Cards| User
```

## 1. Frontend (Neo-Brutalist UI)
- **Technology:** HTML, Vanilla JavaScript/TypeScript, and Tailwind CSS (v3.4 via CDN).
- **Design:** A strict Neo-Brutalist aesthetic featuring high-contrast colors (e.g., `#FFFFF0` backgrounds, `#000000` hard borders, offset shadows) to give the application a distinct, raw look.
- **Interaction:** Communicates asynchronously with the backend API to generate and render itinerary matrix cards dynamically.

## 2. Backend API Gateway
- **Technology:** FastAPI, Uvicorn, Pydantic.
- **Role:** Serves as the bridge between the frontend and the agent engine. 
- **Core Endpoint:** An asynchronous `/api/generate_itinerary` endpoint that ingests user constraints (Vibe Vector, Budget, and Destination) and dispatches the task to the Master Agent.

## 3. Agent Orchestration Engine
- **Technology:** Ollama SDK (for local LLM agent execution) and MCP (Model Context Protocol).
- **Agents:**
  - **Master Agent:** Coordinates the flow, interprets the user vibe, and formats the final payload for the frontend.
  - **Spatial Sub-Agent:** Interfaces with the MCP Server to gather geocoded Points of Interest (POIs) and historical weather, proposing a logical route sequence.
  - **Budget Sub-Agent:** Audits the itinerary against the user's budget constraints.

### A2A Negotiation Loop

```mermaid
sequenceDiagram
    participant Master as Master Agent
    participant Spatial as Spatial Sub-Agent
    participant MCP as FastMCP Server
    participant Budget as Budget Sub-Agent

    Master->>Spatial: Request Itinerary (Destination, Vibe)
    loop Negotiation Loop
        Spatial->>MCP: Fetch POIs & Weather
        MCP-->>Spatial: Return Context Data
        Spatial->>Budget: Propose Route & Estimated Cost
        
        alt Over Budget
            Budget-->>Spatial: Reject (Reason: Cost > Budget Limit)
            Note over Spatial: Adjust Route / Drop expensive POIs
        else Within Budget
            Budget-->>Spatial: Approve (Cost <= Budget Limit)
        end
    end
    
    Spatial-->>Master: Final Approved Itinerary
```

## 4. Context Enrichment (FastMCP Server)
- **Role:** Provides context and external data to the sub-agents.
- **Functions:** Exposes tools such as `get_historical_weather`, `get_points_of_interest`, and `calculate_transit_cost` to ground the LLM's outputs in real-world constraints.