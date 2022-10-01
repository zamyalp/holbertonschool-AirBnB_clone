#!/usr/bin/python3
"""base model for Airbnb clone"""
import uuid
import json
import datetime
import models


class BaseModel:
    """created class for base model"""
    def __init__(self, *args, **kwargs):
        """public instance attributes for BaseModel"""
        timedate_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    break
                elif key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.datetime.strptime(
                        value, timedate_format)
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.strptime(
                            value, timedate_format)
        else:
            self.id = str(uuid.uuid4())
            self.creted_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.strptime()

    def __str__(self) -> str:
        """string ovveride for basemodel"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, slef.__dict__)

    def save(self):
        """updates to current time"""
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """retunr a dcitionary of class instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
