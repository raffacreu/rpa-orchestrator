from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Automation(Base):
    __tablename__ = "automation"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    steps_json = Column(JSON, nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now)
    update_at = Column(DateTime(timezone=True), server_onupdate=func.now)