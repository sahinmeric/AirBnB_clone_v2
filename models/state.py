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
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    if getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            city_list = []
            for ob_id, city in models.storage.all(City).items():
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
