from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Usamos la URL que ya configuraste en tu Docker Compose
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://hbnb_user:hbnb_password@db:5432/hbnb_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # Esta es la madre de todos los modelos de DB

# Función para obtener la sesión (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()