#!/usr/bin/python3
"""file storage engine module"""

import json
from os.path import exists

class FileStorage:
    """rudimentary class for file based data storage"""
    __file_path = 'testdata.json'
    __objects = {}  # type: dict[int, str]

    def all(self):
        """returns objects dictionary"""
        return self.__objects

    def new (self, obj):
        """ stores an object inside the oibject tracker"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """saves a;; object instances to a file"""
        with open(self.__file_path, mode="w",
                  encoding="utf-8") as outinstances:
            json.dump(self.__objects, outinstances)

    def reload(self):
        """deserializes a json-ified object from the filesystem"""
        if exists(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as ininstances:
                self.__objects = json.load(ininstances)
