from sqlalchemy.orm import Session
from typing import Optional, List
from uuid import UUID

from app.domain.models.review import Review
from app.domain.interfaces import ReviewRepository
from app.infrastructure.persistence.models import ReviewModel

class SQLAlchemyReviewRepository(ReviewRepository):
    def __init__(self, db: Session):
        self.db = db # <--- Guardamos la conexión a la DB

    def add(self, review: Review) -> None:
        # 1. Mapeamos: Pasamos de objeto de Dominio a modelo de Tabla
        new_review_db = ReviewModel(
            id=review.id,
            texto=review.texto,
            stars=review.stars,
            user_id=review.user_id,
            place_id=review.place_id,
            created_at=review.created_at,
            updated_at=review.updated_at
        )
        # 2. Guardamos en Postgres
        self.db.add(new_review_db)
        self.db.commit()
        self.db.refresh(new_review_db)

    def get_all(self) -> List[Review]:
        # Traemos todo de la tabla y lo devolvemos
        lista = self.db.query(ReviewModel).all()
        return [Review(
            id=i.id,
            texto=i.texto,
            stars=i.stars,
            user_id=i.user_id,
            place_id=i.place_id,
            created_at=i.created_at
        ) for i in lista]

        # new_lista = list(amenity for amenity in lista == Amenity(amenity))

    def get_by_id(self, review_id: UUID) -> Optional[Review]:
        review = self.db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
        if review == None:
            return None
        review = Review(
                    id=review.id,
                    texto=review.texto,
                    stars=review.stars,
                    user_id=review.user_id,
                    place_id=review.place_id,
                    created_at=review.created_at,
                )
        return review

    def delete(self, review_id: UUID) -> bool:
        review = self.db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
        if review:
            self.db.delete(review)
            self.db.commit()
            return True
        return False

    def update_review(self, data: Review) -> Optional[Review]:
        review_db = self.db.query(ReviewModel).filter(ReviewModel.id == data.id).first()
        if not review_db:
            raise ValueError("Review not found")

        review_db.texto = data.texto
        review_db.stars = data.stars

        self.db.commit()
        self.db.refresh(review_db)

        return Review(
            id=review_db.id,
            texto=review_db.texto,
            stars=review_db.stars,
            user_id=review_db.user_id,
            place_id=review_db.place_id
        )
        

