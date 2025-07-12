from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
import os
from dotenv import load_dotenv

load_dotenv()

oauth2_scheme = HTTPBearer()  # ✅ This enables Bearer token support in Swagger

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    
    try:
        token_str = token.credentials  # ✅ Extract raw token string
        payload = jwt.decode(token_str, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception

    return user
    """

    Dependency to get the current user from the given access token.


    Decodes the given token and extracts the user's ID from the payload.

    Queries the database with the ID to get the user object.


    Raises a 401 error if decoding the token fails or if the user is not found.

    """
