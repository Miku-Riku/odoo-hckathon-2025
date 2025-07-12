from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserOut, UserLogin
from database import SessionLocal
from utils.hashing import hash_password, verify_password
from utils.jwt import create_access_token

router = APIRouter(tags=["Auth"]) 

# Dependency
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
    
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),
        location=user.location,
        availability=user.availability,
        is_public=user.is_public
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if db_user.is_banned:
        raise HTTPException(status_code=403, detail="User is banned")

    token = create_access_token(data={"sub": str(db_user.id), "role": db_user.role.value})
    return {"access_token": token, "token_type": "bearer"}
