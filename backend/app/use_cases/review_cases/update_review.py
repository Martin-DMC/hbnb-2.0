from app.domain.models.review import Review
from app.domain.interfaces import ReviewRepository

class UpdateReview:
    def __init__(self, review_repo: ReviewRepository):
        self.review_repo = review_repo

    def execute(self, review_id: str, data: dict) -> Review:
        review = self.review_repo.get_by_id(review_id)
        if not review:
            raise ValueError("Review_not_found")

    # doble verificacion para evitar problemas con el valor None en la database
    # de esta manera podemos modificar campos unicos si queremos.
        if "texto" in data and data["texto"] is not None:
            review.texto = data["texto"]
        if "stars" in data and data["stars"] is not None:
            review.stars = data["stars"]

        return self.review_repo.update_review(review)

