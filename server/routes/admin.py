from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/ban/{user_id}")
def ban_user(user_id: int, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    if current.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_banned = True
    db.commit()
    return {"message": f"User {user.email} banned."}