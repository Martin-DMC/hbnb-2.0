from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class PlaceBase(BaseModel):
    title: str
    price: float
    longitude: float
    latitude: float
    owner_id: UUID

class CreatePlace(PlaceBase):
        description: str

class PlaceResponse(PlaceBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True

class ShowPlaceResponse(PlaceBase):
    id: UUID
    description: str
    created_at: datetime

    class Config:
        from_attributes = True

class PlaceUpdateSchema(PlaceBase):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None

    class Config:
        from_attributes = True