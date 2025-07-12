from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)