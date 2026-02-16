from sqlalchemy import Column, String, DateTime, Float, ForeignKey, Integer, Table, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .database import Base
import uuid
from datetime import datetime

# tabla intermedia para la relacion many to many de place y amenity
place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", UUID(as_uuid=True), ForeignKey("places.id"), primary_key=True),
    Column("amenity_id", UUID(as_uuid=True), ForeignKey("amenities.id"), primary_key=True),
)

class AmenityModel(Base):
    __tablename__ = "amenities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    places = relationship("PlaceModel", secondary=place_amenity, back_populates="amenities")


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    places = relationship("PlaceModel", back_populates="owner", cascade="all, delete-orphan")
    reviews = relationship("ReviewModel", back_populates="author", cascade="all, delete-orphan")


class PlaceModel(Base):
    __tablename__= "places"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    owner = relationship("UserModel", back_populates="places")
    reviews = relationship("ReviewModel", back_populates="place", cascade="all, delete-orphan")
    amenities = relationship("AmenityModel", secondary=place_amenity, back_populates="places")


class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    texto = Column(String, nullable=False)
    stars = Column(Integer, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    place_id = Column(UUID(as_uuid=True), ForeignKey("places.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship("UserModel", back_populates="reviews")
    place = relationship("PlaceModel", back_populates="reviews")
