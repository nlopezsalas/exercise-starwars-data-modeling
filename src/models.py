import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    startships_id = Column(Integer, ForeignKey('startships.id'), nullable=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    pasajeros = Column(Integer, nullable=False)
    usuarios_favorites = relationship(Favorites)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    people_favorites = relationship(Favorites)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    population = Column(Integer, nullable=False)
    planets_favorites = relationship(Favorites)

class Startships(Base):
    __tablename__ = 'startships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    pasajeros = Column(Integer, nullable=False)
    startships_favorites = relationship(Favorites)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')