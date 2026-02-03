from app.domain.models.place import Place
from app.domain.interfaces import PlaceRepository
from typing import List

class GetAll:
    def __init__(self, place_repo: PlaceRepository):
        self.place_repo = place_repo

    def execute(self) -> List[Place]:
        return self.place_repo.get_all()