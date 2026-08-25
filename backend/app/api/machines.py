from fastapi import APIRouter
from ..models.machine import Machine
from ..services.digital_twin import motor

router = APIRouter(prefix="/machines", tags=["Machines"])

# Temporary in-memory storage
machines = []


@router.post("/")
def register_machine(machine: Machine):
    machines.append(machine)
    return {
        "message": "Machine registered successfully",
        "machine": machine
    }


@router.get("/")
def get_machines():
    return machines


@router.get("/{machine_id}/sensor")
def get_sensor_data(machine_id: str):
    return {
        "machine_id": machine_id,
        **motor.generate_sensor_data()
    }


@router.get("/{machine_id}/history")
def get_machine_history(machine_id: str):
    return {
        "machine_id": machine_id,
        "history": motor.get_history()
    }