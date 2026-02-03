from sqlalchemy.orm import Session
from typing import Optional, List

from app.domain.models.user import User
from app.domain.interfaces import   UserRepository
from app.infrastructure.persistence.models import UserModel

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db # <--- Guardamos la conexión a la DB

    def add(self, user: User) -> None:
        # 1. Mapeamos: Pasamos de objeto de Dominio a modelo de Tabla
        new_user_db = UserModel(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
        # 2. Guardamos en Postgres
        self.db.add(new_user_db)
        self.db.commit()
        self.db.refresh(new_user_db)

    def get_all(self) -> List[User]:
        # Traemos todo de la tabla y lo devolvemos
        lista = self.db.query(UserModel).all()
        return [User(id=i.id, first_name=i.first_name, last_name=i.last_name, email=i.email, created_at=i.created_at) for i in lista]

        # new_lista = list(amenity for amenity in lista == Amenity(amenity))
    def get_by_email(self, email:str) -> Optional[User]:
        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if user == None:
            return None
        user = User(id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    created_at=user.created_at
                )
        return user
