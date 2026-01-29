from abc import ABC, abstractmethod
from app.domain.models.user import User
from app.domain.models.amenity import Amenity
from typing import Optional

class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass


class AmenityRepository(ABC):
    @abstractmethod
    def add(self, amenity: Amenity) -> None:
        pass

    @abstractmethod
    def get_all(self) -> Optional[Amenity]:
        pass