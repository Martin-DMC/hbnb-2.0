from sqlalchemy.orm import Session
from typing import Optional, List
from uuid import UUID

from app.domain.models.place import Place
from app.domain.interfaces import   PlaceRepository
from app.infrastructure.persistence.models import PlaceModel

class SQLAlchemyPlaceRepository(PlaceRepository):
    def __init__(self, db: Session):
        self.db = db # <--- Guardamos la conexión a la DB

    def add(self, place: Place) -> None:
        # 1. Mapeamos: Pasamos de objeto de Dominio a modelo de Tabla
        new_place_db = PlaceModel(
            id=place.id,
            title=place.title,
            description=place.description,
            price=place.price,
            longitude=place.longitude,
            latitude=place.latitude,
            owner_id=place.owner_id,
            created_at=place.created_at,
            updated_at=place.updated_at
        )
        # 2. Guardamos en Postgres
        self.db.add(new_place_db)
        self.db.commit()
        self.db.refresh(new_place_db)

    def get_all(self) -> List[Place]:
        # Traemos todo de la tabla y lo devolvemos
        lista = self.db.query(PlaceModel).all()
        return [Place(
            id=i.id,
            title=i.title,
            description=i.description,
            price=i.price,
            longitude=i.longitude,
            latitude=i.latitude,
            owner_id=i.owner_id,
            created_at=i.created_at,
            updated_at=i.updated_at
        ) for i in lista]

    def get_by_id(self, place_id: UUID) -> Optional[Place]:
    # Traemos todo de la tabla y lo devolvemos
        place = self.db.query(PlaceModel).filter(PlaceModel.id == place_id).first()
        if not place:
            return None
        return Place(
            id=place.id,
            title=place.title,
            description=place.description,
            price=place.price,
            owner_id=place.owner_id,
            longitude=place.longitude,
            latitude=place.latitude,
            created_at=place.created_at,
            updated_at=place.updated_at
        )

    def delete(self, place_id: UUID) -> bool:
        place = self.db.query(PlaceModel).filter(PlaceModel.id == place_id).first()
        if place:
            self.db.delete(place)
            self.db.commit()
            return True
        return False

    def update_place(self, data: Place) -> Place:
        place_db = self.db.query(PlaceModel).filter(PlaceModel.id == data.id).first()
        if not place_db:
            raise ValueError("Place not found")

        place_db.title = data.title 
        place_db.description = data.description
        place_db.price = data.price
        place_db.longitude = data.longitude
        place_db.latitude = data.latitude
        place_db.owner_id = data.owner_id

        self.db.commit()
        self.db.refresh(place_db)

        return Place(
            id=place_db.id,
            title=place_db.title,
            description=place_db.description,
            price=place_db.price,
            longitude=place_db.longitude,
            latitude=place_db.latitude,
            owner_id=place_db.owner_id
        )
