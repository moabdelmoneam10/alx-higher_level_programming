#!/usr/bin/python3
""" CIty model with SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from model_state import Base, State


class City(Base):
    """ City model
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    state = relationship("State", backref='cities')
