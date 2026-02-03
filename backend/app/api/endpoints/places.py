from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.api.schemas.place_schemas import CreatePlace, PlaceResponse
from app.use_cases.place_cases.create_place import Create_Place
from app.use_cases.place_cases.show_all import GetAll
from app.infrastructure.persistence.sql_Achemy.sql_place import SQLAlchemyPlaceRepository, Session
from app.infrastructure.persistence.database import get_db

router = APIRouter()


@router.post("/", response_model=PlaceResponse)
def create_place(data: CreatePlace, db: Session = Depends(get_db)):
    try:
    # Ahora el repo recibe la 'db' de FastAPI
        repo = SQLAlchemyPlaceRepository(db) 
        use_case = Create_Place(repo)
        new_place = use_case.execute(
            title=data.title,
            description=data.description,
            price=data.price,
            longitude=data.longitude,
            latitude=data.latitude
        )
        return new_place
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[PlaceResponse])
def show_all(db: Session = Depends(get_db)):
    repo = SQLAlchemyPlaceRepository(db) 
    use_case = GetAll(repo)
    return use_case.execute()
        
