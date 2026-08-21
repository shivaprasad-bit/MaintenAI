from pydantic import BaseModel, Field
from typing import Literal

class Machine(BaseModel):
    machine_id: str = Field(..., examples=["MTR-001"])
    name: str = Field(..., examples=["Assembly Motor"])
    machine_type: Literal["motor", "pump", "compressor", "cnc"]
    location: str = Field(..., examples=["Plant A - Line 1"])