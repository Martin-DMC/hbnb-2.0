from fastapi import APIRouter, HTTPException, Depends
from app.api.schemas import UserCreate, UserResponse
from app.use_cases.register_user import RegisterUser
from app.infrastructure.persistence.mem_user_repository import InMemoryUserRepository

router = APIRouter()

fake_repo = InMemoryUserRepository()

@router.post("/", response_model=UserResponse)
def register_user(user_in: UserCreate):
    use_case = RegisterUser(fake_repo)
    try:
        new_user = use_case.execute(
            email=user_in.email,
            password=user_in.password,
            first_name=user_in.first_name,
            last_name=user_in.last_name
        )
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))