from sqlalchemy.orm import Session
from typing import Optional, List
from uuid import UUID

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
            is_admin=user.is_admin,
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
        return [User(
            id=i.id,
            first_name=i.first_name,
            last_name=i.last_name,
            email=i.email,
            created_at=i.created_at
        ) for i in lista]

        # new_lista = list(amenity for amenity in lista == Amenity(amenity))
    def get_by_email(self, email:str) -> Optional[User]:
        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if user == None:
            return None
        user = User(id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    password=user.password,
                    email=user.email,
                    created_at=user.created_at
                )
        return user

    def get_by_id(self, user_id:UUID ) -> Optional[User]:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user == None:
            return None
        user = User(id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    created_at=user.created_at
                )
        return user

    def delete(self, user_id: UUID) -> bool:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

    def update_user(self, data: User) -> User:
        user_db = self.db.query(UserModel).filter(UserModel.id == data.id).first()
        if not user_db:
            raise ValueError("User not found")

        user_db.first_name = data.first_name 
        user_db.last_name = data.last_name
        user_db.email = data.email
        user_db.password = data.password
        user_db.is_admin = data.is_admin

        self.db.commit()
        self.db.refresh(user_db)

        return User(
            id=user_db.id,
            email=user_db.email,
            first_name=user_db.first_name,
            last_name=user_db.last_name,
            password=user_db.password
        )
        
