from app.domain.models.amenity import Amenity
from app.domain.interfaces import AmenityRepository

class CreateAmenity:
    def __init__(self, amenity_repo: AmenityRepository):
        self.amenity_repo = amenity_repo

    def execute(self, name: str) -> Amenity:
        new_amenity = Amenity(name=name)

        self.amenity_repo.add(new_amenity)

        return new_amenity
