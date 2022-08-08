#!/usr/bin/python3
"""This module defines a Baseclass for all models in our Airbnb clone"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """The BaseModel from which future models will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    elif key == "updated_at":
                        self.updated_at = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()

    def __str__(self):
        """string representation of the basemodel"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
            of __dict__.
        """
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
