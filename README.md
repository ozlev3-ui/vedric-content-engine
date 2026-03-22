# Vedric Content Engine

Project skeleton for a monorepo that includes:

- `backend`: FastAPI API service
- `frontend`: Next.js + TailwindCSS web app
- `workers`: Python worker process
- `docker`: Docker Compose setup for local development
- `docs`: project documentation

## Prerequisites

- Docker + Docker Compose
- (Optional) Python 3.12+
- (Optional) Node.js 20+

## Quick start with Docker

1. Copy environment templates:
   ```bash
   cp .env.example .env
   cp backend/.env.example backend/.env
   cp frontend/.env.local.example frontend/.env.local
   cp workers/.env.example workers/.env
   ```
2. Start the stack:
   ```bash
   docker compose -f docker/docker-compose.yml up --build
   ```
3. Access services:
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000
   - Backend health: http://localhost:8000/health

## Run services without Docker

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Worker

```bash
cd workers
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/main.py
```

## Notes

This repository only contains the initial project skeleton. Business logic and full system features are intentionally not implemented yet.

## Agent Architecture (Backend)

A Hebrew-first, placeholder agent pipeline is scaffolded under `backend/app/agents` and prompt templates under `backend/app/ai/prompts/he`.

Included agents:

1. AudienceArchitect
2. ContentStrategist
3. ScenarioRefiner
4. HookGenerator
5. AnchorWriter
6. LeadMagnetBuilder
7. ContentAtomizer
8. ReelsAgent
9. StoriesAgent
10. PostsAgent
11. ContentScheduler

All agents currently expose structured input/output interfaces and load placeholder Hebrew prompt templates for future LLM implementation.


### Ollama (Agent LLM)

Set these backend environment variables to enable LLM calls from agents:

```bash
OLLAMA_MODEL=qwen2.5:7b
OLLAMA_URL=http://localhost:11434/api/generate
```

The `HookGenerator` agent now demonstrates Ollama usage with graceful fallback when Ollama is unavailable.
