#!/usr/bin/python3
"""Test cases for the BaseModel class"""


from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """Class that inherits from testcase class"""

    def test_initialization(self):
        """Tests constructor of class"""
        base = BaseModel()
        base.name = "My First Model"
        base.number = 89
        self.assertIs(type(base), BaseModel)
        self.assertEqual(base.name, "My First Model")
        self.assertEqual(base.number, 89)

    def test_str_representation(self):
        """Tests string representation of instance of class"""
        base_1 = BaseModel()
        base_string = f"[BaseModel] ({base_1.id}) {base_1.__dict__}"
        self.assertEqual(base_string, str(base_1))
