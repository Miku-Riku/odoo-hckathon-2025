from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserOut
from database import SessionLocal
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed = pwd_context.hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed,
        location=user.location,
        availability=user.availability,
        is_public=user.is_public
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
