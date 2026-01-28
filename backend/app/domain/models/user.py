from dataclasses import dataclass
from .base_model import BaseModel

@dataclass
class User(BaseModel):
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    is_admin: bool = False
