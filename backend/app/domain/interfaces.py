from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID, uuid4

from app.domain.models.user import User
from app.domain.models.amenity import Amenity
from app.domain.models.place import Place


class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    def get_by_id(self, id: uuid4) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

class PlaceRepository(ABC):
    @abstractmethod
    def add(self, place: Place) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Place]:
        pass

class AmenityRepository(ABC):
    @abstractmethod
    def add(self, amenity: Amenity) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Amenity]:
        pass

    @abstractmethod
    def get(self, name: str) -> Optional[Amenity]:
        pass
