#!/usr/bin/python3
"""Class that stores city info on users"""


from models.base_model import BaseModel


class City(BaseModel):
    """Cities class that inherits from BaseModel"""
    state_id = ""
    name = ""
