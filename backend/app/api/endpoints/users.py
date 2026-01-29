from fastapi import APIRouter, HTTPException, Depends
from app.api.schemas import UserCreate, UserResponse, AmenityCreate, AmenityResponse
from app.use_cases.register_user import RegisterUser, CreateAmenity
from app.infrastructure.persistence.mem_user_repository import InMemoryUserRepository, InMemoryAmenitiesRepository

router = APIRouter()
amenity_router = APIRouter()

fake_repo = InMemoryUserRepository()
fake_repo_amenity = InMemoryAmenitiesRepository()

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
    

@router.post("/", response_model=AmenityResponse)
def create_amenity(amenity_in: AmenityCreate):
    use_case_a = CreateAmenity(fake_repo_amenity)
    try:
        new_amenity = use_case_a.execute(name=amenity_in.name)
        return new_amenity
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))