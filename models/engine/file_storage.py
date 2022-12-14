#!/usr/bin/python3
"""
HBNB CLONE
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import json
import os.path


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        public instance that returns the dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
        public instance methods that set in
        objects the obj with key
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj = json.load(f)
            for k, v in obj.items():
                class_name = k.split('.')[0]
                self.__objects[k] = eval(class_name)(**v)
        except BaseException:
            pass
