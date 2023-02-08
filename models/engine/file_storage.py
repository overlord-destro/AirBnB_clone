#!/usr/bin/python3
"""JSON file management module"""

import json

from models.base_model import BaseModel


class FileStorage:
    """File storage class

    Description:
        This class adds a persistent capability to the project by
        serialising and deserialising model instances into json file
        and deserialises JSON file into an instance of a model
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get object

        Description:
            This method obtains the dictionary object of a model

        Returns:
            A dictionary object of the model
        """

        return self.__objects

    def new(self, obj):
        """Populate object values

        Description:
            This method sets into the dictionary object the object
            value passed to it as parameter

        Args:
            obj (dict): the object to set
        """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serialise object

        Description:
            This method serialises the model instance to a JSON file

        """
        
        object_storage = {}

        with open(self.__file_path, "w", encoding="UTF-8") as file:

            for key, value in self.__objects.items():
                object_storage[key] = value.to_dict()
            json.dump(object_storage, file)

