from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

@dataclass
class BaseModel:
    """clase base con valores repetibles"""
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def touch(self):
        """Actualiza el timestamp de modificacion"""
        self.updated_at = datetime.utcnow()

@dataclass
class User(BaseModel):
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    is_admin: bool = False


@dataclass
class Place(BaseModel):
    title: str = ""
    description: str = ""
    price: float = 0.0
    longitude: float = 0.0
    latitude: float = 0.0
    owner_id: UUID = None
    amenities: list = field(default_factory=list)

@dataclass
class Review(BaseModel):
    place_id: UUID = None
    user_id: UUID = None
    text: str = ""
    stars: int = 0

@dataclass
class Amenities(BaseModel):
    Name: str = ""