from fastapi import APIRouter, HTTPException, Depends
from app.api.schemas import AmenityCreate, AmenityResponse
from app.use_cases.create_amenity import CreateAmenity
from app.infrastructure.persistence.sql_amenity_repository import SQLAlchemyAmenityRepository, Session
from app.infrastructure.persistence.database import get_db

router = APIRouter()


@router.post("/", response_model=AmenityResponse)
def create_amenity(data: AmenityCreate, db: Session = Depends(get_db)):
    try:
    # Ahora el repo recibe la 'db' de FastAPI
        repo = SQLAlchemyAmenityRepository(db) 
        use_case = CreateAmenity(repo)
        return use_case.execute(data.name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))