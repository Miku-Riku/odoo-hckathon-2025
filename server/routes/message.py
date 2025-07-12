from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.dependencies import get_db, get_current_user
from models.user import User
from models.message import Message
from schemas.message import MessageCreate, MessageOut

router = APIRouter(prefix="/message", tags=["Message"])

@router.post("/broadcast")
def broadcast_message(msg: MessageCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can broadcast")
    message = Message(content=msg.content)
    db.add(message)
    db.commit()
    return {"message": "Broadcast sent"}

@router.get("/all", response_model=list[MessageOut])
def get_messages(db: Session = Depends(get_db)):
    return db.query(Message).order_by(Message.timestamp.desc()).all()