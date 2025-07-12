from pydantic import BaseModel
from typing import Optional

class FeedbackCreate(BaseModel):
    swap_id: int
    to_user_id: int
    rating: int
    comment: Optional[str]

class FeedbackOut(BaseModel):
    id: int
    swap_id: int
    from_user_id: int
    to_user_id: int
    rating: int
    comment: Optional[str]

model_config = {
    "from_attributes": True
}
