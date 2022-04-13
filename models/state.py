#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'fs':
        name = ""

        @property
        def cities(self):
            """ getter for the list of cities of states"""
            city_list = []
            new_dict = models.storage.all(City)
            for key, obj in new_dict.items():
                if self.id == obj.state_id:
                    city_list.append(obj)
            return city_list
