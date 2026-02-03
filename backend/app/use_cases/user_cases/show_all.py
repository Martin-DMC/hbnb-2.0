from app.domain.models.user import User
from app.domain.interfaces import UserRepository
from typing import List

class GetAll:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self) -> List[User]:
        return self.user_repo.get_all()
