from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.api.schemas.user_schemas import UserCreate, UserResponse
from app.use_cases.user_cases.register_user import RegisterUser
from app.use_cases.user_cases.show_all import GetAll
from app.use_cases.user_cases.delete_user import DeleteUser
from app.infrastructure.persistence.sql_Achemy.sql_user import SQLAlchemyUserRepository, Session
from app.infrastructure.persistence.database import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=UserResponse)
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    try:
        repo = SQLAlchemyUserRepository(db)
        use_case = RegisterUser(repo)
        new_user = use_case.execute(
            email=data.email,
            password=data.password,
            first_name=data.first_name,
            last_name=data.last_name
        )
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=List[UserResponse])
def show_all(db: Session = Depends(get_db)):
    repo = SQLAlchemyUserRepository(db) 
    use_case = GetAll(repo)
    return use_case.execute()

@router.delete("/{user_id}", status_code=204)
def delete_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    user_repo = SQLAlchemyUserRepository(db)
    delete_use_case = DeleteUser(user_repo)
    
    if not delete_use_case.execute(user_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return None
        