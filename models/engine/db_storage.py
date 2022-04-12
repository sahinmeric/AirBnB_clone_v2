#!/usr/bin/python3
""" DB storage"""

from audioop import add
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """ DBS storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
        usr = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(usr, passwd, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Lists all the objects of given class
        or every objects if the class is not given
        """
        objects = []
        if cls is None:
            classes = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
            objs = []
            for _class in classes:
                query = self.__session.query(eval(_class))
                for res in query:
                    objs.append(res)
        else:
            objs = self.__session.query(cls).all()
        for value in objs:
            key = type(value).__name__+'.'+str(value.id)
            objects[key] = value
        return objects

    def new(self, obj):
        """adds the object to the current db session"""
        if obj:
            self.__session.add(add)

    def save(self):
        """saves the current session to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the obj from the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all the tables in the db and starts the session"""
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(ses)
        self.__session
