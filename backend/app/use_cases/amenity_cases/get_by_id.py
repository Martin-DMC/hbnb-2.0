from app.domain.models.amenity import Amenity
from app.domain.interfaces import AmenityRepository
from typing import Optional

class GetById:
    def __init__(self, amenity_repo: AmenityRepository):
        self.amenity_repo = amenity_repo

    def execute(self, amenity_id: str) -> Optional[Amenity]:
        return self.amenity_repo.get_by_id(amenity_id=amenity_id) or None
