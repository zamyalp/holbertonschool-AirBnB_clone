#!/usr/bin/python3
"""makes class for place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """stores data for place"""
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
