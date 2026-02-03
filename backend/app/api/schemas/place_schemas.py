from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PlaceBase(BaseModel):
    title: str
    price: float
    longitude: float
    latitude: float

class CreatePlace(PlaceBase):
        description: str

class PlaceResponse(PlaceBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True