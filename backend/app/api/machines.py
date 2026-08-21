from fastapi import APIRouter
from ..models.machine import Machine

router = APIRouter(prefix="/machines", tags=["Machines"])

machines_db = []

@router.post("/")
def register_machine(machine: Machine):
    machines_db.append(machine)
    return {
        "message": "Machine registered successfully",
        "machine": machine
    }

@router.get("/")
def get_machines():
    return machines_db