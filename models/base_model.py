#!/usr/bin/python3
"""
HBNB CLONE
"""

import uuid
from datetime import datetime 

class BaseModel():
    """
    Class BaseModel that define all commun 
    attribute methods for other class
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs: 
            for k, v in kwargs.items():
                if k == "id":
                    self.id = str(v)
                elif k == "created_at":
                    self.created_at = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == "updated_at":
                    self.updated_at =  datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')

   




    def __str__(self):
        """
        print
        """
        return "[{}] ({}) {}". format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        public instance methods 
        that updat the piblic instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values 
        """

        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['updated_at'] = str(self.updated_at.isoformat())
        self.__dict__['id'] = str(uuid.uuid4())
        self.__dict__['created_at'] = self.created_at.isoformat()

        return self.__dict__
