from sqlalchemy.orm import Session
from typing import Optional, List

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
            created_at=i.created_at,
            updated_at=i.updated_at
        ) for i in lista]
