#!/usr/bin/python3
"""Test cases for the file storage class"""

import unittest

from models.engine.file_storage import FileStorage

class TestFileStorageInitialisation(unittest.TestCase):
    """Test cases for initialising the file storage class"""

    def test_file_path(self):
        """Test case for the private __file_path attribute"""
        return self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_private_object_attribute(self):
        """Test case for the private __object attribute"""
        return self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_class_init_with_arg(self):
        """Test case for initialising class with an arg"""
        with self.assertRaises(TypeError):
            FileStorage(object)

class TestFileStorage(unittest.TestCase):
    """Test cases for all methods of the file storage class"""

    def test_return_object_type(self):
        """Test case for the type of object returned by all() method"""
        obj = FileStorage().all()
        return self.assertTrue(type(obj) is dict)
