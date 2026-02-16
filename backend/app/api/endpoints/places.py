from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.api.schemas.place_schemas import CreatePlace, PlaceResponse, PlaceUpdateSchema, ShowPlaceResponse
from app.use_cases.place_cases.create_place import Create_Place
from app.use_cases.place_cases.show_all import GetAll
from app.use_cases.place_cases.get_by_id import GetById
from app.use_cases.place_cases.delete_place import DeletePlace
from app.use_cases.place_cases.update_place import UpdatePlace
from app.infrastructure.persistence.sql_Achemy.sql_place import SQLAlchemyPlaceRepository, Session
from app.infrastructure.persistence.database import get_db
from app.core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=PlaceResponse)
def create_place(
    data: CreatePlace,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)):
    try:
    # Ahora el repo recibe la 'db' de FastAPI
        repo = SQLAlchemyPlaceRepository(db) 
        use_case = Create_Place(repo)
        new_place = use_case.execute(
            title=data.title,
            description=data.description,
            price=data.price,
            longitude=data.longitude,
            latitude=data.latitude,
            owner_id=data.owner_id
        )
        return new_place
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[PlaceResponse])
def show_all(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    repo = SQLAlchemyPlaceRepository(db) 
    use_case = GetAll(repo)
    return use_case.execute()

@router.get("/{place_id}", response_model=ShowPlaceResponse)
def show_place(
    place_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    repo = SQLAlchemyPlaceRepository(db) 
    use_case = GetById(repo)
    return use_case.execute(place_id)

@router.delete("/{place_id}", status_code=204)
def delete_place(
    place_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    place_repo = SQLAlchemyPlaceRepository(db)
    delete_use_case = DeletePlace(place_repo)

    # VERIFICACION PARA OWNER ID Y CURRENT USER ID
    # if current_place.id != place_id:
    #     raise HTTPException(status_code=403)

    if not delete_use_case.execute(place_id):
        raise HTTPException(status_code=404, detail="Place no encontrado")
    return None

@router.put("/{place_id}", response_model=PlaceResponse)
def update_place(
    place_id: str,
    data: PlaceUpdateSchema,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # convertimos el ID del token a str para hacer una comparacion limpia 
    # if str(current_place.id) != str(place_id):
    #     raise HTTPException(status_code=403, detail="unauthorized")

    repo = SQLAlchemyPlaceRepository(db)
    use_case = UpdatePlace(repo)
    
    try:
        # Convertimos el Schema a dict pero solo los campos que el usuario mandó
        # esta manera se llama hidratacion. 
        update_data = data.model_dump(exclude_unset=True) 
        return use_case.execute(place_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

