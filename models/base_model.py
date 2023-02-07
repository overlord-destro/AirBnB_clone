#!/usr/bin/python3
"""BaseModel class from which all other classes inherit"""


from uuid import uuid4
from datetime import datetime, timedelta


class BaseModel():
    def __init__(self, *args, **kwargs):
        """
        Constructor for the BaseModel class
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of Instance of BaseModel classs
        """
        output = "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return output

    def save(self):
        """
        Updates updated_at variable to moment of usage
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary representaion of instance with all attributes
        """
        newdict = self.__dict__.copy()
        newdict['__class__'] = self.__class__.__name__
        newdict['created_at'] = self.__dict__['created_at'].isoformat()
        newdict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return newdict
