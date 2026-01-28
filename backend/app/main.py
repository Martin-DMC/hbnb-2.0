from fastapi import FastAPI
from app.api.endpoints.users import router as user_router

app = FastAPI(title="hBnb Remastered API")

app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def health_check():
    return {"status": "ok", "message": "hBnb API is running"}