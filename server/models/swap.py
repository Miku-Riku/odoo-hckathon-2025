from sqlalchemy import Column, Integer, ForeignKey, Enum, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum

class SwapStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    cancelled = "cancelled"

class Swap(Base):
    __tablename__ = "swaps"
    id = Column(Integer, primary_key=True)
    requester_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    message = Column(String)
    status = Column(Enum(SwapStatus), default=SwapStatus.pending)
    created_at = Column(DateTime, default=datetime.utcnow)