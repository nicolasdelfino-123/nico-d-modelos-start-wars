import os
from datetime import datetime, timezone
from eralchemy2 import render_er
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Column, ForeignKey, String, DateTime
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(40), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(40), nullable=False)
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True)
    created: Mapped[str] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    favorites = relationship('Favorite', backref='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "full_name": self.full_name,
            "email": self.email,
            "created": self.created.isoformat()
        }


class Planet(db.Model):
    __tablename__ = 'planet'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    diameter: Mapped[str] = mapped_column(String(100), nullable=False)
    rotation_period: Mapped[str] = mapped_column(String(100), nullable=False)
    orbital_period: Mapped[str] = mapped_column(String(100), nullable=False)
    gravity: Mapped[str] = mapped_column(String(100), nullable=False)
    population: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped[str] = mapped_column(String(100), nullable=False)
    terrain: Mapped[str] = mapped_column(String(100), nullable=False)
    surface_water: Mapped[str] = mapped_column(String(100), nullable=False)
    created = Column(DateTime, default=lambda: datetime.now(
        timezone.utc), nullable=False)
    edited = Column(DateTime, default=lambda: datetime.now(
        timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    favorites = relationship('Favorite', backref='planet', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created.isoformat() if self.created else None,
            "edited": self.edited.isoformat() if self.edited else None
        }


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    vehicle_class: Mapped[str] = mapped_column(String(100), nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(100), nullable=False)
    length: Mapped[str] = mapped_column(String(100), nullable=False)
    cost_in_credits: Mapped[str] = mapped_column(String(100), nullable=False)
    crew: Mapped[str] = mapped_column(String(100), nullable=False)
    max_atmosphering_speed: Mapped[str] = mapped_column(
        String(100), nullable=False)
    cargo_capacity: Mapped[str] = mapped_column(String(100), nullable=False)
    consumables: Mapped[str] = mapped_column(String(100), nullable=False)
    url: Mapped[str] = mapped_column(String(200), nullable=False)
    created = Column(DateTime, default=lambda: datetime.now(
        timezone.utc), nullable=False)
    edited = Column(DateTime, default=lambda: datetime.now(
        timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    favorites = relationship('Favorite', backref='vehicle', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "length": self.length,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "url": self.url,
            "created": self.created.isoformat() if self.created else None,
            "edited": self.edited.isoformat() if self.edited else None
        }


class People(db.Model):
    __tablename__ = 'people'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(100), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[str] = mapped_column(String(100), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(100), nullable=False)
    height: Mapped[str] = mapped_column(String(20), nullable=False)
    mass: Mapped[str] = mapped_column(String(40), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(20), nullable=False)
    homeworld: Mapped[str] = mapped_column(String(40), nullable=False)
    url: Mapped[str] = mapped_column(String(100), nullable=False)
    created = Column(DateTime, default=lambda: datetime.now(
        timezone.utc), nullable=False)
    edited = Column(DateTime, default=lambda: datetime.now(
        timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    favorites = relationship('Favorite', backref='people', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "homeworld": self.homeworld,
            "url": self.url,
            "created": self.created.isoformat() if self.created else None,
            "edited": self.edited.isoformat() if self.edited else None
        }


class Favorite(db.Model):
    __tablename__ = 'favorite'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    people_id: Mapped[int] = mapped_column(
        ForeignKey('people.id'), nullable=True)
    vehicle_id: Mapped[int] = mapped_column(
        ForeignKey('vehicle.id'), nullable=True)
    planet_id: Mapped[int] = mapped_column(
        ForeignKey('planet.id'), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "vehicle_id": self.vehicle_id,
            "planet_id": self.planet_id
        }


render_er(db.Model, 'diagram.png')
