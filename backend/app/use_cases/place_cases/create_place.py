from app.domain.models.place import Place
from app.domain.interfaces import PlaceRepository
from uuid import UUID

class Create_Place:
    def __init__(self, place_repo: PlaceRepository):
        self.place_repo = place_repo

    def execute(self,
                title: str,
                description: str,
                price: float,
                longitude: float,
                latitude: float,
                owner_id: UUID
        ) -> Place:

        new_place = Place(
            title=title,
            description=description, 
            price=price,
            longitude=longitude,
            latitude=latitude,
            owner_id=owner_id
        )

        self.place_repo.add(new_place)
        
        return new_place
