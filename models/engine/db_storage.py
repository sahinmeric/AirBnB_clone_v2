#!/usr/bin/python3
""" DB storage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base


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
        dic_obj = []
        classes = {'State': State, 'City': City, 'User': User,
                   'Place': Place, 'Review': Review, "Amenity": Amenity}

        if cls is None:
            for k, v in classes.items():
                query = self.__session.query(v).all()
                for obj in query:
                    dic_obj[obj.__class__.__name__ + "." + str(obj.id)] = obj

        else:
            query = self.__session.query(cls).all()
            for obj in query:
                dic_obj[obj.__class__.__name__ + "." + str(obj.id)] = obj
        return dic_obj

    def new(self, obj):
        """adds the object to the current db session"""
        if obj:
            self.__session.add(obj)

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
        Session = scoped_session(ses)
        self.__session = Session()

    def close(self):
        """Json to obj"""
        self.__session.close()
