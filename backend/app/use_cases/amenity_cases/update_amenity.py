from app.domain.models.amenity import Amenity
from app.domain.interfaces import AmenityRepository
from app.core.security import myctx

class UpdateAmenity:
    def __init__(self, amenity_repo: AmenityRepository):
        self.amenity_repo = amenity_repo

    def execute(self, amenity_id: str, data: dict) -> Amenity:
        amenity = self.amenity_repo.get_by_id(amenity_id)
        if not amenity:
            raise ValueError("Amenity_not_found")

    # doble verificacion para evitar problemas con el valor None en la database
    # de esta manera podemos modificar campos unicos si queremos.
        if "name" in data and data["name"] is not None:
            amenity.name = data["name"]
        
        return self.amenity_repo.update_amenity(amenity)

