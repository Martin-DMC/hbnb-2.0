from dataclasses import dataclass
from .base_model import BaseModel
from uuid import UUID

@dataclass
class Review(BaseModel):
    place_id: UUID = None
    user_id: UUID = None
    text: str = ""
    stars: int = 0
    