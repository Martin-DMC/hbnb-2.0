from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.api.schemas.review_schema import ReviewCreate, ReviewResponse, ReviewUpdateSchema
from app.use_cases.review_cases.create_review import CreateReview
from app.use_cases.review_cases.show_all import GetAll
from app.use_cases.review_cases.delete_review import DeleteReview
from app.use_cases.review_cases.update_review import UpdateReview
from app.infrastructure.persistence.sql_Achemy.sql_review import SQLAlchemyReviewRepository, Session
from app.infrastructure.persistence.database import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=ReviewResponse)
def create_review(
        data: ReviewCreate,
        db: Session = Depends(get_db)
    ):
    try:
        repo = SQLAlchemyReviewRepository(db)
        use_case = CreateReview(repo)
        new_review = use_case.execute(
            texto=data.texto,
            stars=data.stars,
        )
        return new_review
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=List[ReviewResponse])
def show_all(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(status_code=401)

    repo = SQLAlchemyReviewRepository(db) 
    use_case = GetAll(repo)
    return use_case.execute()

@router.delete("/{review_id}", status_code=204)
def delete(
    review_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    review_repo = SQLAlchemyReviewRepository(db)
    delete_use_case = DeleteReview(review_repo)

    # HERE WE'LL MAKING THE VERIFY OF CURRENT USER AND USER ID OF REVIEW  
    # if current_user.id != user_id:
    #     raise HTTPException(status_code=403)

    if not delete_use_case.execute(review_id):
        raise HTTPException(status_code=404, detail="Review no encontrado")
    return None

@router.put("/{review_id}", response_model=ReviewResponse)
def update_review(
    review_id: str,
    data: ReviewUpdateSchema,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # HERE WILL TO BE THE VERIFY OF CURRENT USER ID AND THE ID'S USER OF REVIEW
    # convertimos el ID del token a str para hacer una comparacion limpia 
    # if str(current_user.id) != str(user_id):
    #     raise HTTPException(status_code=403, detail="unauthorized")

    repo = SQLAlchemyReviewRepository(db)
    use_case = UpdateReview(repo)
    
    try:
        # Convertimos el Schema a dict pero solo los campos que el usuario mandó
        # esta manera se llama hidratacion. 
        update_data = data.model_dump(exclude_unset=True) 
        return use_case.execute(review_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
