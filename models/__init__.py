#!/usr/bin/python3
""" initializes an instance of the data storage class"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
