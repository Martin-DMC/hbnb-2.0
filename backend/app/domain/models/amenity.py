from dataclasses import dataclass
from .base_model import BaseModel

@dataclass
class Amenities(BaseModel):
    Name: str = ""
