#!/usr/bin/python3
"""file storage engine module"""

import json
from os.path import exists
import models

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
        with open(self.__file_path, mode="w", encoding="utf-8") as outinstances:
            json.dump(
                {
                    k: (v.to_dict() if not isinstance(v, dict) else v)
                    for (k, v) in self._objects.items()
                }, outinstances)

    def reload(self):
        """deserializes a json-ified object from the filesystem"""
        if exists(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as ininstances:
                old_instances = json.load(ininstances)
                for key in old_instances:
                    self.__objects[key] = getattr(
                        models,
                        old_instances[key]['__class__'])(**old_instances[key])
