from abc import ABC, abstractmethod
from app.domain.models.user import User
from typing import Optional

class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass