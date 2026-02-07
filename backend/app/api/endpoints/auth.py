from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.use_cases.login_user import LoginUser
from app.infrastructure.persistence.sql_Achemy.sql_user import SQLAlchemyUserRepository, Session
from app.infrastructure.persistence.database import get_db

router = APIRouter()

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user_repo = SQLAlchemyUserRepository(db)
    login_use_case = LoginUser(user_repo)

    result = login_use_case.execute(email=form_data.username, password=form_data.password)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return result