from app.domain.models.amenity import Amenity
from app.domain.interfaces import AmenityRepository
from typing import List

class GetAll:
    def __init__(self, amenity_repo: AmenityRepository):
        self.amenity_repo = amenity_repo

    def execute(self) -> List[Amenity]:
        return self.amenity_repo.get_all()
