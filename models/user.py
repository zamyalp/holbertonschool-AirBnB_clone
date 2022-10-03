#!/usr/bin/python3
"""contains data for user module"""


from models.base_model import BaseModel


class User(BaseModel):
    """class representing User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
