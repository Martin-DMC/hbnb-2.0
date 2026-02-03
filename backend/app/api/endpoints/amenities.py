from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.api.schemas.amenity_schema import AmenityCreate, AmenityResponse
from app.use_cases.amenity_cases.create_amenity import CreateAmenity
from app.use_cases.amenity_cases.show_all import GetAll
from app.use_cases.amenity_cases.get_by_name import GetByName
from app.infrastructure.persistence.sql_Achemy.sql_amenity import SQLAlchemyAmenityRepository, Session
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

@router.get("/", response_model=List[AmenityResponse])
def show_all(db: Session = Depends(get_db)):
    repo = SQLAlchemyAmenityRepository(db) 
    use_case = GetAll(repo)
    return use_case.execute()
        

@router.get("/{name}", response_model=AmenityResponse)
def get_by_name(name: str, db: Session = Depends(get_db)):

    repo = SQLAlchemyAmenityRepository(db) 
    use_case = GetByName(repo)
    amenity = use_case.execute(name=name) 
    if amenity is None:
        raise HTTPException(status_code=404, detail="amenity no encontrada")
    else:
        return amenity
