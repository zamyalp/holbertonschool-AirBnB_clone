#!/usr/bin/python3
"""base model for Airbnb clone"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """created class for base model"""

    def __init__(self, *args, **kwargs):
        """initiliazer"""

        if kwargs: 
            for key, value in kwargs.items():
                if "created_at" in kwargs:
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if "updated_at" in kwargs:
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.updated_at = self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """string ovveride for basemodel"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates to current time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """retunr a dcitionary of class instance"""

        return dict(self.__dict__,
                __class__=self.__class__.__name__,
                updated_at=str(self.updated_at.isoformat()),
                created_at=str(self.created_at.isoformat()))
