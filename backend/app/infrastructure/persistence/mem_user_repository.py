from app.domain.models.user import User
from app.domain.models.amenity import Amenity
from app.domain.repositories import UserRepository, AmenityRepository
from typing import List, Optional

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: List[User] = []

    def add(self, user: User) -> None:
        self._users.append(user)

    def get_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self._users if u.email == email), None)

class InMemoryAmenitiesRepository(AmenityRepository):
    def __init__(self):
        self._amenities: List[Amenity] = []

    def add(self, amenity: Amenity) -> None:
        self._amenities.append(amenity)

    def get_all(self) -> List[Amenity]:
        return self._amenities