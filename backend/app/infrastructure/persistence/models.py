from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from .database import Base
import uuid
from datetime import datetime

class AmenityModel(Base):
    __tablename__ = "amenities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)