from app.domain.interfaces import PlaceRepository

class DeletePlace:
    def __init__(self, place_repo: PlaceRepository):
        self.place_repo = place_repo

    def execute(self, place_id: str) -> bool:
        # Aquí podrías meter lógica de "Solo el admin borra" o algo así
        return self.place_repo.delete(place_id)