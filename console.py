#!/usr/bin/python3
"""Command line interface implementation"""

import cmd
import shlex

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for command line interface"""

    objects = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    prompt = "(hbnb) "

    def default(self, param):
        """Default method"""

        cmds = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
                }

        values = param.split(".", 1)
        obj_name = values[0]

        if obj_name in self.objects and len(values) >= 2:
            values = "".join(values[1:]).split("(")
            obj_method = values[0]
            if obj_method in cmds and len(values) >= 2:
                obj_args = " ".join(tuple("".join(values[1:])[:-1].split(", ")))
                cmds[obj_method]("{} {}".format(obj_name, obj_args))
        else:
            print("Unknown syntax: {}".format(param))

    def do_quit(self, line):
        """Quits console

        Description:
            This method exits the console upon entering of prompt

        Returns:
            True upon exit
        """

        return True

    def do_EOF(self, line):
        """Quits console

        Description:
            This method is similar to the do_quit method. While this
            method is inbuilt, the do_quit is the custom implementation
            of this method
        """

        return True

    def emptyline(self):
        """Pass

        Description:
            This method overrides the inbuilt emptyline method and
            executes nothing when nothing is typed. When the enter key
            is pressed, the cursor jumps to the next line
        """

        pass

    def do_create(self, line):
        """Create new instance of BaseModel

        Description:
            This method creates a new instance of the base model when
            invoked and prints its id to the stdout. If the parameter
            is not equivalent to class BaseModel, it prints an enrror
            message '*** class doesn't exist ** '
        """

        if line:
            if line not in HBNBCommand.objects:
                print("** class doesn't exist **")
            else:
                inst = HBNBCommand.objects[line]()
                inst.save()
                print(inst.id)
        else:
            print("** class name missing **")

    def do_show(self, params):
        """Print instance representation

        Description:
            This method prints the string representation of an instance
            based on the class name and the id. It splits the elements
            in the args parameter into a list. It then assigns the list
            elements to named variables with which will be used to
            fetch instance data

        """

        values = params.split(" ")

        if not values[0]:
            print("** class name missing **")
        elif values[0] not in HBNBCommand.objects:
            print("** class doesn't exist **")
        elif len(values) < 2:
            print("** instance id missing **")
        else:
            object_name = values[0]
            object_id = values[1]

            try:
                objs = object_name + "." + object_id
                inst_obj = storage._FileStorage__objects[objs]
                print(inst_obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, params):
        """Delete an instance

        Description:
            This method deletes an instance based on the class name
            and the id. It implements the same approach as the do_show,
            deletes an instance by its id and updates the file with the
            save() method from the file storage class
        """

        values = params.split(" ")

        if not values[0]:
            print("** class name missing **")
        elif values[0] not in HBNBCommand.objects:
            print("** class doesn't exist **")
        elif not values[1]:
            print("** instance id missing **")
        else:
            object_name = values[0]
            object_id = values[1]

            try:
                objs = object_name + "." + object_id
                del storage.all()[objs]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, param=""):
        """Print all instances

        Description:
            This method prints all string representation of
            instances either based on the instance name or not.
        """
        values = param.split(" ")

        if param != "":
            if values[0] not in HBNBCommand.objects:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    print(v, end="")

        else:
            object_name = values[0]

            for k, v in storage.all().items():
                if k.startswith(object_name):
                    print(v, end="")

    def do_update(self, param):
        """Update an instance

        Description:
            This method updates an instance of a model based on the
            class name and id. Usuage:

            update <class name> <id> <attribute name> "<attribute value>
        """

        values = shlex.split(param)

        if len(param) < 1:
            print("** class name missing **")
        elif values[0] not in HBNBCommand.objects:
            print("** class doesn't exist **")
        elif len(param) < 2:
            print("** instance id missing **")
        else:
            objs = values[0] + "." + values[1]

            if objs not in storage.all():
                print("** no instance found **")
            elif len(param) < 3:
                print("** attribute name missing **")
            elif len(param) < 4:
                print("** value missing **")
            else:
                storage.all()[objs].save()


#   ======================================================================

if __name__ == "__main__":
    HBNBCommand().cmdloop()
