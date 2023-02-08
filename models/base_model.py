#!/usr/bin/python3
"""Base module with methods common to all the modules that inherit from it"""

from uuid import uuid4
from datetime import datetime, timedelta


class BaseModel():
    """Base class

    Description:
        This class is the base model from which all other models
        inherit properties. It hosts all the attributes or methods
        that are common to the other classes

    """

    def __init__(self, *args, **kwargs):
        """Initialise class

        Description:
            This method initialises the class with id, and the date
            and time the instance is created and updated.

        """

        #from models import storage

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ("created_at", "updated_at"):
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            #storage.new(self)

    def __str__(self):
        """Print string representation of model

        Description:
            This method prints a string representation of the model
            instance. The printed data include name of the class,
            the id of the instance model and a dictionary of other
            attributes of the model instance

        """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update date time value

        Description:
            This method updates the updated_at date time value for this
            model. It changes to the current date time anytime the
            model is updated

        """
        from models import storage

        self.updated_at = datetime.now()
        #storage.save()

    def to_dict(self):
        """Create dictionary representation

        Description:
            This method creates a dictionary representation of the
            model instance. This dictionary contains the name of the
            class, the date and time it was created and last updated.

        Returns:
            A dictionary representation of the model instance

        """

        newdict = self.__dict__.copy()
        newdict['__class__'] = self.__class__.__name__
        newdict['created_at'] = self.__dict__['created_at'].isoformat()
        newdict['updated_at'] = self.__dict__['updated_at'].isoformat()

        return newdict
