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

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    
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
        self.update_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values 
        """
        
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['update_at'] = self.update_at.isoformat()
        self.__dict__['id'] = self.id
        self.__dict__['created_at'] = self.created_at.isoformat()

        return self.__dict__
