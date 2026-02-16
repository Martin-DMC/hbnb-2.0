from app.domain.models.review import Review
from app.domain.interfaces import ReviewRepository
from typing import List

class GetAll:
    def __init__(self, review_repo: ReviewRepository):
        self.review_repo = review_repo

    def execute(self) -> List[Review]:
        return self.review_repo.get_all()
