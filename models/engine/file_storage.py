#!/usr/bin/python3
"""
HBNB CLONE
"""


from models.base_model import BaseModel
import json
import os.path

class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """

    """ def __init__(self, file_path="", objects=None):
        self.file_path = file_path
       self.objects = {}
    """
    __file_path = "file.json"
    __objects = {}

    """ 
    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        if not isinstance(value, str):
            raise TypeError("file_path must be an String")
        self.__file_path = value

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        if not isinstance(value, dict):
            raise TypeError("objects must be an dict")
        self.__objects = value
    """    

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
        public instance that serializes
        objects to the json file
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "w") as f:
                json.dump(objdict, f)

    """
    def reload(self):

       public instance that deserializes the json file

        file_name = self.__file_path
        if os.path.exists(file_name):
            with open(file_name, "w") as jsonFile:
                self.__objects = json.load(file_name)
    """
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

