from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.api.schemas.amenity_schema import AmenityCreate, AmenityResponse, AmenityUpdateSchema
from app.use_cases.amenity_cases.create_amenity import CreateAmenity
from app.use_cases.amenity_cases.show_all import GetAll
from app.use_cases.amenity_cases.get_by_name import GetByName
from app.use_cases.amenity_cases.update_amenity import UpdateAmenity
from app.use_cases.amenity_cases.delete_amenity import DeleteAmenity
from app.infrastructure.persistence.sql_Achemy.sql_amenity import SQLAlchemyAmenityRepository, Session
from app.infrastructure.persistence.database import get_db
from app.core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=AmenityResponse)
def create_amenity(
    data: AmenityCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
    # Ahora el repo recibe la 'db' de FastAPI
        repo = SQLAlchemyAmenityRepository(db) 
        use_case = CreateAmenity(repo)
        return use_case.execute(data.name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[AmenityResponse])
def show_all(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    repo = SQLAlchemyAmenityRepository(db) 
    use_case = GetAll(repo)
    return use_case.execute()
        

@router.get("/{name}", response_model=AmenityResponse)
def get_by_name(
    name: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    repo = SQLAlchemyAmenityRepository(db) 
    use_case = GetByName(repo)
    amenity = use_case.execute(name=name) 
    if amenity is None:
        raise HTTPException(status_code=404, detail="amenity no encontrada")
    else:
        return amenity

@router.put("/{amenity_id}", response_model=AmenityResponse)
def update_amenity(
    amenity_id: str,
    data: AmenityUpdateSchema,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # convertimos el ID del token a str para hacer una comparacion limpia 
    # if str(current_user.id) != str(user_id):
    #     raise HTTPException(status_code=403, detail="unauthorized")

    repo = SQLAlchemyAmenityRepository(db)
    use_case = UpdateAmenity(repo)
    
    try:
        # Convertimos el Schema a dict pero solo los campos que el usuario mandó
        # esta manera se llama hidratacion. 
        update_data = data.model_dump(exclude_unset=True) 
        return use_case.execute(amenity_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{amenity_id}", status_code=204)
def delete_amenity(
    amenity_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    amenity_repo = SQLAlchemyAmenityRepository(db)
    use_case = DeleteAmenity(amenity_repo)

    # if current_user.id != user_id:
    #     raise HTTPException(status_code=403)

    if not use_case.execute(amenity_id):
        raise HTTPException(status_code=404, detail="Amenity no encontrada")
    return None
