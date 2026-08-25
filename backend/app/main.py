from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.machines import router as machine_router

app = FastAPI(
    title="MaintenAI API",
    description="Industrial Machine Maintenance Intelligence System",
    version="1.0.0"
)

# Allow React frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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