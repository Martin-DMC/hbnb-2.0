from fastapi import FastAPI

app = FastAPI(title="hBnb Remastered API")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "hBnb API is running"}