from fastapi import FastAPI

app = FastAPI(
    title="DevOps Platform Lab",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to DevOps Platform Lab"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }