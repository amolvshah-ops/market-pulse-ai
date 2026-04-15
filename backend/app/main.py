from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Market Pulse AI Backend",
    version="0.1.0",
    description="Backend API for a multi-agent trading application."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Market Pulse AI backend is running",
        "status": "ok"
    }

@app.get("/health")
def health():
    return {
        "service": "backend",
        "status": "healthy"
    }

@app.get("/api/v1/agents")
def list_agents():
    return {
        "agents": [
            "technical",
            "sentiment",
            "ml",
            "risk"
        ]
    }
