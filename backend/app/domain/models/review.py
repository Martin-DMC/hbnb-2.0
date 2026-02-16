from dataclasses import dataclass
from .base_model import BaseModel
from uuid import UUID
from typing import Optional

@dataclass
class Review(BaseModel):
    place_id: UUID = None
    user_id: UUID = None
    texto: str = ""
    stars: int = 0
    