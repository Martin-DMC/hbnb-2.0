from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class AmenityCreate(BaseModel):
    name: str

class AmenityResponse(BaseModel):
    id: UUID
    name: str
    created_at: datetime

    class Config:
        from_attributes = True