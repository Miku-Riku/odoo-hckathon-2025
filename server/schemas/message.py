from pydantic import BaseModel
from datetime import datetime

class MessageOut(BaseModel):
    id: int
    content: str
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }

class MessageCreate(BaseModel):
    content: str
