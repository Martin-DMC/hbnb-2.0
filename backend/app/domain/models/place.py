from dataclasses import dataclass, field
from uuid import UUID
from .base_model import BaseModel

@dataclass
class Place(BaseModel):
    title: str = ""
    description: str = ""
    price: float = 0.0
    longitude: float = 0.0
    latitude: float = 0.0
    owner_id: UUID = None
    amenities: list[UUID] = field(default_factory=list)
    review: list = field(default_factory=list)