from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from app.domain.models.user import User
from app.domain.models.amenity import Amenity
from app.domain.models.place import Place
from app.domain.models.review import Review


class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Optional[User]:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def delete(self, user_id: UUID) -> bool:
        pass

    @abstractmethod
    def update_user(self, data: User) -> User:
        pass

class PlaceRepository(ABC):
    @abstractmethod
    def add(self, place: Place) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Place]:
        pass

    @abstractmethod
    def get_by_id(self, place_id: UUID) -> Optional[Place]:
        pass

    @abstractmethod
    def delete(self, place_id: UUID) -> bool:
        pass

    @abstractmethod
    def update_place(self, data: Place) -> Place:
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

    @abstractmethod
    def get_by_id(self, amenity_id: UUID) -> Optional[Amenity]:
        pass

    @abstractmethod
    def update_amenity(self, name: str) -> Optional[Amenity]:
        pass

class ReviewRepository(ABC):
    @abstractmethod
    def add(self, review: Review) -> None:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Optional[Review]:
        pass

    @abstractmethod
    def get_all(self) -> List[Review]:
        pass

    @abstractmethod
    def delete(self, review_id: UUID) -> bool:
        pass

    @abstractmethod
    def update_review(self, data: Review) -> Review:
        pass
