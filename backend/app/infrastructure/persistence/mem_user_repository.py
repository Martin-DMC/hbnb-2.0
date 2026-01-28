from app.domain.models.user import User
from app.domain.repositories import UserRepository
from typing import List, Optional

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: List[User] = []

    def add(self, user: User) -> None:
        self._users.append(user)

    def get_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self._users if u.email == email), None)