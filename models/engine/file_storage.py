#!/usr/bin/python3
"""
HBNB CLONE
"""


import json


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file 
    and deserializes JSON file to instances:
    """
    def __init__(self, file_path, objects):
        self.file_path = file_path
        self.objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        if type(value) is not str:
            raise TypeError("file_path must be an String")
        self.__file_path = value

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        if type(value) is not dict:
            raise TypeError("objects must be an dict")
        self.__objects = value
        
    def all(self):
        """

        """
        return self.__objects

    def new(self, obj):
        """"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """

        """
        fileName = self.__file_path
        
        with open(fileName, "w") as jsonFile:
            json.dump(self.__objects, fileName)
            
    def reload(self):
        """

        """
        fileName = self.__file_path
        
        with open(fileName, "w") as jsonFile:
            self.__objects = json.load(fileName)


        



