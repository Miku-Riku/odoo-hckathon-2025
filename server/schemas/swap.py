from pydantic import BaseModel
from enum import Enum
from typing import Optional

class SwapStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    cancelled = "cancelled"

class SwapCreate(BaseModel):
    receiver_id: int
    message: Optional[str] = ""

class SwapOut(BaseModel):
    id: int
    requester_id: int
    receiver_id: int
    message: str
    status: SwapStatus

    model_config = {
        "from_attributes": True
    }
