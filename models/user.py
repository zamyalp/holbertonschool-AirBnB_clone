#!/usr/bin/python3
""" creates user class data"""
from models.base_model import BaseModel


class User(BaseModel):
    """sotres user data in object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
