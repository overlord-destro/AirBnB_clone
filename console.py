#!/usr/bin/python3
"""Command line interface implementation"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for command line interface"""

    objects = {"BaseModel": BaseModel}

    prompt = "(hbnb) "

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
            if line != "BaseModel":
                print("** class doesn't exist **")
            else:
                inst = BaseModel()
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
        object_name = values[0]
        object_id = values[1]

        if not object_name:
            print("** class name missing **")
        elif object_name not in HBNBCommand.objects:
            print("** class doesn't exist **")
        elif not object_id:
            print("** instance id missing **")
        else:
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
        object_name = values[0]
        object_id = values[1]

        if not object_name:
            print("** class name missing **")
        elif object_name not in HBNBCommand.objects:
            print("** class doesn't exist **")
        elif not object_id:
            print("** instance id missing **")
        else:
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
        object_name = values[0]

        print("[\"", end="")
        if param != "":
            if object_name not in HBNBCommand.objects:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    print(v, end="")
                print("\"]")

        else:
            for k, v in storage.all().items():
                if k.startswith(object_name):
                    print(v, end="")
            print("\"]")


#   ======================================================================

if __name__ == "__main__":
    HBNBCommand().cmdloop()
