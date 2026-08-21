from fastapi import FastAPI
from .api.machines import router as machine_router

app = FastAPI(
    title="MaintenAI API",
    description="Industrial Machine Maintenance Intelligence System",
    version="1.0.0"
)

app.include_router(machine_router)

@app.get("/")
def root():
    return {
        "message": "MaintenAI Backend is running.",
        "status": "healthy"
    }

@app.get("/health")
def health():
    return {"status": "OK"}