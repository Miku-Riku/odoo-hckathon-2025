from pydantic import BaseModel, EmailStr
from typing import Optional, List
from enum import Enum

class Role(str, Enum):
    user = "user"
    admin = "admin"

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    location: Optional[str]
    availability: List[str] = []
    is_public: Optional[bool] = True
    offered_skills: List[str] = []
    wanted_skills: List[str] = []

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    location: Optional[str]
    availability: List[str]
    is_public: bool
    offered_skills: List[str]
    wanted_skills: List[str]
    role: Role

    model_config = {
        "from_attributes": True
    }