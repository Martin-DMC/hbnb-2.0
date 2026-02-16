from dataclasses import dataclass, field
from .base_model import BaseModel

@dataclass
class User(BaseModel):
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    is_admin: bool = False
    places: list = field(default_factory=list)
    reviews: list = field(default_factory=list)
