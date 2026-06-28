# WRANGLER — Product Requirement Document v2.2.0

**Project:** Wrangler (Autonomous Co-Traveler Agent for Solo Adventurers)  
**Author:** Neeraj Ojha  
**Version:** 2.2.0  
**Last Updated:** 2026-06-28  
**Status:** Approved

---

## 1. Executive Summary & Core Mission

Wrangler is an **autonomous, offline-first, privacy-respecting** travel companion engineered for solo travelers, backpackers, and extreme outdoor adventurers. It consolidates real-time weather intelligence, interactive cartography, economic accommodation sourcing, AI-powered itinerary generation, survival planning, and cultural immersion into a single high-contrast interface.

### Core Product Tenet: *"Structure the Chaos"*

Solo adventuring is highly dynamic. Weather shifts in minutes, plans collapse at borders, routes get blocked by landslides, and connectivity vanishes in canyons. Wrangler acts as a **digital trail boss** — not a sponsored booking portal — that:

1. **Operates offline-first** via local LLM inference (Ollama) and progressive caching
2. **Respects privacy absolutely** — zero telemetry, zero cloud data uploads
3. **Optimizes for survival conditions** — high-contrast UI, minimal battery drain, emergency protocols
4. **Filters commercial noise** — LLM-powered result re-ranking bypasses sponsored upsells

---

## 2. System Architecture

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        WRANGLER FRONTEND (PWA)                              │
│  [ Neo-Brutalist UI | Leaflet.js | jsPDF | Service Worker | IndexedDB ]     │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │ REST + Server-Sent Events (SSE)
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        WRANGLER BACKEND (Flask)                             │
│  [ Routing | Data Validation | Generator Functions (SSE) | SQLite ]         │
└────────┬──────────────┬───────────────┬──────────────┬──────────────────────┘
         │              │               │              │
         ▼              ▼               ▼              ▼
┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────────────────┐
│ OpenWeather  ││  Open-Meteo  ││ Booking.com  ││    Ollama Engine         │
│  API (Live)  ││  (Fallback)  ││  (RapidAPI)  ││ (Qwen3.5 → Phi-3 → Gemma)│
└──────────────┘└──────────────┘└──────────────┘└──────────────────────────┘
                                                         │
                                                         ▼
                                                ┌──────────────────┐
                                                │  FastMCP Server  │
                                                │  (Tool Registry) │
                                                └──────────────────┘
```

### 2.2 Tech Stack

| Layer | Technology | Justification |
|-------|-----------|---------------|
| **Runtime** | Python 3.11+ | Ecosystem maturity, Ollama SDK support |
| **Backend** | Flask | Lightweight micro-framework, easy setup, supports generators for SSE |
| **LLM Engine** | Ollama (Qwen3.5:latest) | Local inference, zero cloud dependency, model flexibility |
| **Agent Protocol** | FastMCP (Model Context Protocol) | Standardized tool-use interface for LLM agents |
| **Database** | SQLite | Zero-config, file-based, offline-first |
| **Frontend** | Vanilla HTML/JS + Vite (build) | Minimal bundle size (< 150KB gzip), zero framework overhead |
| **CSS** | Tailwind CSS | Utility-first styling to rapidly implement the Neo-Brutalist design system |
| **Mapping** | Leaflet.js + OpenStreetMap + leaflet-offline | Free tiles, offline caching, custom styling |
| **Weather** | OpenWeatherMap (primary) + Open-Meteo (fallback) | Dual-source redundancy, Open-Meteo requires no API key |
| **Accommodation** | Booking.com (via RapidAPI) | Comprehensive global accommodation data |
| **PDF** | jsPDF (client-side) | Offline-capable, no server dependency |
| **Offline** | Service Worker + Workbox + IndexedDB (Dexie.js) | Progressive caching, offline-first data persistence |

---

## 3. Feature Specifications

### FR-1: Real-Time Atmospheric Intelligence

**Priority:** P0 (Critical)  
**Dependencies:** OpenWeatherMap API, Open-Meteo API

Retrieve micro-climate telemetry for any city worldwide, with LLM-interpreted trail advisories.

### FR-2: Cartographic Visualization & POI Indexing

**Priority:** P0 (Critical)  
**Dependencies:** Leaflet.js, OpenStreetMap, OpenWeather Geocoding

Render an interactive, high-contrast map with dynamic markers for landmarks, trails, accommodations, and emergency services. Includes offline tile caching.

### FR-3: Economic Accommodation Sourcing

**Priority:** P1 (High)  
**Dependencies:** Booking.com API (via RapidAPI)

Query real-time lodging availability and prices, then apply LLM-powered re-ranking to bypass commercial bias and surface genuinely optimal options based on safety, utility, and location.

### FR-4: Generative Adventure Architect & Budget Calculator

**Priority:** P0 (Critical)  
**Dependencies:** Ollama (Qwen3.5), FastMCP tools, FR-1 weather data

Generate a granular, day-by-day itinerary with dynamic budget allocation, personalized to the traveler's vibe. Utilizes a multi-agent negotiation loop (Master, Spatial, Budget agents) to ensure the route is logical and affordable.

### FR-5: Survival & Emergency Response Protocol

**Priority:** P0 (Critical)  
**Dependencies:** Ollama, Geocoding data, OSM Overpass API, Curated DB

> [!IMPORTANT]
> This feature generates life-safety information. High accuracy is paramount.

#### Description
One-click SOS plan generator providing localized emergency contacts, nearest medical facilities, and terrain-specific survival guidance.

#### Verification Pipeline
1. **Primary Database:** A curated, version-controlled JSON database containing verified national emergency numbers (e.g., 911, 112).
2. **Live Verification:** Cross-validates hospital locations using the OpenStreetMap Overpass API and Nominatim geocoding.
3. **LLM Synthesis:** Ollama generates contextual survival guidance grounded in the verified data, assigning confidence scores.
4. **Data Tagging:** Each piece of information in the output is tagged: `✅ Verified` (DB/API sourced), `⚠️ AI-Generated` (LLM tips), or `🔄 Unverified`.

### FR-6: Dynamic Packing Matrix & PDF Export

**Priority:** P1 (High)  
**Dependencies:** Ollama, jsPDF, weather data

Generate a terrain-aware, climate-adjusted packing list organized by survival priority, exportable as a styled PDF generated entirely client-side.

### FR-7: Cultural & Historical Narrative Companion

**Priority:** P1 (High)  
**Dependencies:** Ollama (Qwen3.5)

An interactive conversational companion that provides contextual cultural intelligence — local history, folk stories, language phrases, social etiquette, and food recommendations.

### FR-8: Trip Journal & Data Export

**Priority:** P2 (Medium)  
**Dependencies:** IndexedDB, jsPDF

Allow travelers to log daily notes, photos, and expenses during the trip. Export the entire trip as a structured journal PDF or JSON.

### FR-9: Multi-City Route Planner

**Priority:** P2 (Medium)  
**Dependencies:** FR-4 (itinerary generator), Leaflet.js

Plan multi-leg journeys across 2-5 cities with inter-city transit estimation and budget allocation per leg.

---

## 4. UI/UX Design System

- **Primary Palette:** Soft Ivory (`#FFFFF0`), Pure Black (`#000000`), Safety Yellow (`#FFE600`), Danger Red (`#FF3366`).
- **Typography:** High-contrast, heavy monospace fonts (Fira Code, JetBrains Mono).
- **Structural Borders:** Hard-edged, 3px solid black borders.
- **Shadows:** Flat, un-blurred block shadows.

## 5. Deployment Strategy

- **Local:** Docker Compose configuration to spin up Flask, Ollama, and the frontend dev server.
- **Database:** Local SQLite file for backend persistence.
