from app.domain.models.review import Review
from app.domain.interfaces import ReviewRepository

class CreateReview:
    def __init__(self, review_repo: ReviewRepository):
        self.review_repo = review_repo

    def execute(self, texto: str, stars: int) -> Review:
        # existing_user = self.review_repo.get_by_email(email)
        # if existing_user:
        #     raise ValueError("El email ya está registrado")

        # passwor_hash = myctx.hash(password)
        new_review = Review(
            texto=texto,
            stars=stars
            )

        self.review_repo.add(new_review)
        
        return new_review

