from sqlalchemy.orm import Session
from typing import Optional
from uuid import UUID
from app.domain.models.amenity import Amenity
from app.domain.interfaces import AmenityRepository
from app.infrastructure.persistence.models import AmenityModel # modelo de tabla

class SQLAlchemyAmenityRepository(AmenityRepository):
    def __init__(self, db: Session):
        self.db = db # <--- Guardamos la conexión a la DB

    def add(self, amenity: Amenity) -> None:
        # 1. Mapeamos: Pasamos de objeto de Dominio a modelo de Tabla
        new_amenity_db = AmenityModel(
            id=amenity.id,
            name=amenity.name,
            created_at=amenity.created_at,
            updated_at=amenity.updated_at
        )
        # 2. Guardamos en Postgres
        self.db.add(new_amenity_db)
        self.db.commit()
        self.db.refresh(new_amenity_db)

    def get_all(self) -> list[Amenity]:
        # Traemos todo de la tabla y lo devolvemos
        lista = self.db.query(AmenityModel).all()
        return [Amenity(id=i.id, name=i.name, created_at=i.created_at) for i in lista]

        # new_lista = list(amenity for amenity in lista == Amenity(amenity))
    def get(self, name: str) -> Optional[Amenity]:
        amenity = self.db.query(AmenityModel).filter(AmenityModel.name == name).first()
        if amenity == None:
            return None
        amenity = Amenity(id=amenity.id, name=amenity.name, created_at=amenity.created_at)
        return amenity

    def update_amenity(self, amenity: Amenity) -> Amenity:
        amenity_db = self.db.query(AmenityModel).filter(AmenityModel.id == amenity.id).first()
        if not amenity_db:
            raise ValueError("Amenity not found")

        amenity_db.name = amenity.name

        self.db.commit()
        self.db.refresh(amenity_db)

        return Amenity(
            id=amenity_db.id,
            name=amenity_db.name
        )
        
    def get_by_id(self, amenity_id: UUID) -> Amenity:
    # Traemos todo de la tabla y lo devolvemos
        amenity = self.db.query(AmenityModel).filter(AmenityModel.id == amenity_id).first()
        if not amenity:
            return None
        return Amenity(
            id=amenity.id,
            name=amenity.name,
            )

    def delete(self, amenity_id: UUID) -> bool:
        amenity = self.db.query(AmenityModel).filter(AmenityModel.id == amenity_id).first()
        if amenity:
            self.db.delete(amenity)
            self.db.commit()
            return True
        return False
