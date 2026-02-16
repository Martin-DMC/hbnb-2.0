from app.domain.models.place import Place
from app.domain.interfaces import PlaceRepository

class UpdatePlace:
    def __init__(self, place_repo: PlaceRepository):
        self.place_repo = place_repo

    def execute(self, place_id: str, data: dict) -> Place:
        place = self.place_repo.get_by_id(place_id)
        if not place:
            raise ValueError("place_not_found")

    # doble verificacion para evitar problemas con el valor None en la database
    # de esta manera podemos modificar campos unicos si queremos.
        if "title" in data and data["title"] is not None:
            place.title = data["title"]
        if "price" in data and data["price"] is not None:
            place.price = data["price"]
        if "description" in data and data["description"] is not None:
            place.description = data["description"]
        if "longitude" in data and data["longitude"] is not None:
            place.longitude = data["longitude"]
        if "latitude" in data and data["latitude"] is not None:
            place.latitude = data["latitude"]
        
        return self.place_repo.update_place(place)

