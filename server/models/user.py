from sqlalchemy import Column, Integer, String, Boolean, ARRAY, Enum
from database import Base
import enum

class RoleEnum(str, enum.Enum):
    user = "user"
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    location = Column(String)
    profile_photo_url = Column(String)
    availability = Column(ARRAY(String))
    is_public = Column(Boolean, default=True)
    role = Column(Enum(RoleEnum), default=RoleEnum.user)
    is_banned = Column(Boolean, default=False)
