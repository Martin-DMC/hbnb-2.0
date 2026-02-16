from app.domain.interfaces import ReviewRepository

class DeleteReview:
    def __init__(self, review_repo: ReviewRepository):
        self.review_repo = review_repo

    def execute(self, review_id: str) -> bool:
        # Aquí podrías meter lógica de "Solo el admin borra" o algo así
        return self.review_repo.delete(review_id)