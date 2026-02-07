from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt, JWTError
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.infrastructure.persistence.database import get_db
from app.infrastructure.persistence.sql_Achemy.sql_user import SQLAlchemyUserRepository

SECRET_KEY = os.getenv("SECRET_KEY", "My-SuPeR-ClAvE-PaRa-ReMaStEr")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# le dice a FastAPI que el token viene en el header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# hash de la contraseña
myctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(subject: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:

    return myctx.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Genera un hash a partir de una contraseña"""
    return myctx.hash(password)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido o expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # 1. Decodificamos el token usando tu SECRET_KEY
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        
        if email is None:
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception

    # 2. Verificamos que el usuario realmente exista en la DB
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_email(email=email)
    
    if user is None:
        raise credentials_exception
        
    return user
