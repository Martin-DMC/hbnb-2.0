from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class ReviewBase(BaseModel):
    texto: str
    stars: int

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True

class ReviewUpdateSchema(ReviewBase):
    texto: Optional[str] = None
    stars: Optional[int] = None

    class Config:
        from_attributes = True