from fastapi import APIRouter, Depends, HTTPException
from utils.dependencies import get_current_user, get_db
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserOut

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/me", response_model=UserOut)
def read_my_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/search", response_model=list[UserOut])
def search_users(skill: str, db: Session = Depends(get_db)):
    return db.query(User).filter(
        User.is_public == True,
        (User.offered_skills.any(skill) | User.wanted_skills.any(skill))
    ).all()

@router.post("/report_skill")
def report_skill(user_id: int, skill: str, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if skill not in user.offered_skills:
        raise HTTPException(status_code=400, detail="Skill not found")
    if skill not in user.reported_skills:
        user.reported_skills.append(skill)
        db.commit()
    return {"message": "Skill reported"}