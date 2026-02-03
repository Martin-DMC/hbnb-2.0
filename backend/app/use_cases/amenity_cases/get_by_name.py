from app.domain.models.amenity import Amenity
from app.domain.interfaces import AmenityRepository
from typing import Optional

class GetByName:
    def __init__(self, amenity_repo: AmenityRepository):
        self.amenity_repo = amenity_repo

    def execute(self, name:str) -> Optional[Amenity]:
        return self.amenity_repo.get(name=name) or None
