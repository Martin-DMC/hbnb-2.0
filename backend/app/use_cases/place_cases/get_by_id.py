from app.domain.models.place import Place
from app.domain.interfaces import PlaceRepository

class GetById:
    def __init__(self, place_repo: PlaceRepository):
        self.place_repo = place_repo

    def execute(self, place_id: str) -> Place:
        return self.place_repo.get_by_id(place_id)