#!/usr/bin/python3
"""Test cases for the BaseModel class"""


from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """Class that inherits from testcase class"""
    
    def test_initialization(self):
        """Tests constructor of class"""
        b1 = BaseModel()
        b1.name = "My First Model"
        b1.number = 89
        self.assertIs(type(b1), BaseModel)
        self.assertEqual(b1.name, "My First Model")
        self.assertEqual(b1.number, 89)

    def test_str_representation(self):
        """Tests string representation of instance of class"""
        b2 = BaseModel()
        b2_string = "[BaseModel] ({}) {}".format(b2.id, b2.__dict__)
        self.assertEqual(b2_string, str(b2))
