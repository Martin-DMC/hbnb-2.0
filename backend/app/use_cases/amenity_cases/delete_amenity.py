from app.domain.interfaces import AmenityRepository

class DeleteAmenity:
    def __init__(self, amenity_repo: AmenityRepository):
        self.amenity_repo = amenity_repo

    def execute(self, amenity_id: str) -> bool:
        # Aquí podrías meter lógica de "Solo el admin borra" o algo así
        return self.amenity_repo.delete(amenity_id)