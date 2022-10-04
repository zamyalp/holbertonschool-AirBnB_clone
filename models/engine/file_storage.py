#!/usr/bin/python3
"""file storage engine module"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place





class FileStorage:
    """rudimentary class for file based data storage"""
    __file_path = 'tdata.json'
    __objects = {}

    def all(self):
        """returns all objects"""
        return self.__objects

    def new (self, obj):
        """ stores an object inside the oibject tracker"""
        key = obj.__class__.__name + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """saves all object instances to a file"""
        my_dict = {}
        for key in self.__objects:
            my_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
                json.dump(my_dict, f)
                

    def reload(self):
        """converts json to python object"""
        try:
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f)
            for key in new_dict:
                class_name = new_dict[key]["__class__"]
                self.__objects[key] = class_keys[class_name](**new_dict[key])
        except FileNotFoundError:
            pass
