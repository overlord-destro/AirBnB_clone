#!/usr/bin/python3
"""Test cases for the BaseModel class"""


from datetime import datetime
from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """Test cases for base model class"""

    def test_initialization(self):
        """Test case for constructor of class"""
        base = BaseModel()
        base.name = "My First Model"
        base.number = 89
        self.assertIs(type(base), BaseModel)
        self.assertEqual(base.name, "My First Model")
        self.assertEqual(base.number, 89)

    def test_id_of_instance(self):
        """Test case for id of an instance of base model"""
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))

    def test_unique_id_of_instances(self):
        """Test case for the uniqueness of id of instances"""
        base_1 = BaseModel()
        base_2 = BaseModel()
        self.assertNotEqual(base_1.id, base_2.id)

    def test_id_type(self):
        """Test case for the type of id, which is a string"""
        base = BaseModel()
        self.assertTrue(isinstance(base.id, str))

    def test_created_at_is_datetime(self):
        """Test case for created_at is datetime"""
        base = BaseModel()
        self.assertTrue(isinstance(base.created_at, datetime))

    def test_updated_at_is_datetime(self):
        """Test case for updated_at is datetime"""
        base = BaseModel()
        self.assertTrue(isinstance(base.updated_at, datetime))

    def test_str_representation(self):
        """Tests string representation of instance of class"""
        base_1 = BaseModel()
        base_string = f"[BaseModel] ({base_1.id}) {base_1.__dict__}"
        self.assertEqual(base_string, str(base_1))
