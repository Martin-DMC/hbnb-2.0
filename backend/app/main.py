from fastapi import FastAPI
from app.infrastructure.persistence.database import engine, Base
from app.api.endpoints.users import router as user_router
from app.api.endpoints.amenities import router as amenity_router
from app.api.endpoints.places import router as place_router
from app.api.endpoints.reviews import router as review_router
from app.api.endpoints import users, auth

Base.metadata.create_all(bind=engine)


app = FastAPI(title="hBnb Remastered API")

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(amenity_router, prefix="/amenities", tags=["amenities"])
app.include_router(place_router, prefix="/places", tags=["places"])
app.include_router(review_router, prefix="/review", tags=["review"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/")
def health_check():
    return {"status": "ok", "message": "hBnb API is running"}