from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

class AmenityCreate(BaseModel):
    name: str

class AmenityResponse(BaseModel):
    id: UUID
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


class AmenityUpdateSchema(BaseModel):
    name: Optional[str] = None

    class Config:
        from_attributes = True