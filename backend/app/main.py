from fastapi import FastAPI
from app.infrastructure.persistence.database import engine, Base
from app.api.endpoints.users import router as user_router
from app.api.endpoints.amenities import router as amenity_router

Base.metadata.create_all(bind=engine)


app = FastAPI(title="hBnb Remastered API")

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(amenity_router, prefix="/amenities")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "hBnb API is running"}