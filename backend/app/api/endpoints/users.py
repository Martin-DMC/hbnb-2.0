from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.api.schemas.user_schemas import UserCreate, UserResponse, UserUpdateSchema
from app.use_cases.user_cases.register_user import RegisterUser
from app.use_cases.user_cases.show_all import GetAll
from app.use_cases.user_cases.delete_user import DeleteUser
from app.use_cases.user_cases.update_user import UpdateUser
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
def show_all(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(status_code=401)
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

    if current_user.id != user_id:
        raise HTTPException(status_code=403)

    if not delete_use_case.execute(user_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return None

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: str,
    data: UserUpdateSchema,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # convertimos el ID del token a str para hacer una comparacion limpia 
    if str(current_user.id) != str(user_id):
        raise HTTPException(status_code=403, detail="unauthorized")

    repo = SQLAlchemyUserRepository(db)
    use_case = UpdateUser(repo)
    
    try:
        # Convertimos el Schema a dict pero solo los campos que el usuario mandó
        # esta manera se llama hidratacion. 
        update_data = data.model_dump(exclude_unset=True) 
        return use_case.execute(user_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
