import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorites_characters = Table('favorites_characters', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)


favorites_planets = Table('favorites_planets', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('planet_id', Integer, ForeignKey('planet.id'))
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    favorite_characters = relationship('Character', secondary=favorites_characters, back_populates='favorited_by')
    favorite_planets = relationship('Planet', secondary=favorites_planets, back_populates='favorited_by')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
