#!/usr/bin/python3
"""Class Review that stores info on reviews by users"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
