from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.dependencies import get_db, get_current_user
from models.feedback import Feedback
from schemas.feedback import FeedbackCreate, FeedbackOut
from models.user import User

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post("/submit", response_model=FeedbackOut)
def submit_feedback(data: FeedbackCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    feedback = Feedback(
        swap_id=data.swap_id,
        from_user_id=user.id,
        to_user_id=data.to_user_id,
        rating=data.rating,
        comment=data.comment
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback
