#!/usr/bin/python3
"""Command line interface implementation"""

import cmd
import shlex
from shlex import split
import re

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """Class for command line interface"""

    prompt = "(hbnb) "
    storage = models.storage

    objects = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def parse(self, arg):

        curly_braces = re.search(r"\{(.*?)\}", arg)
        brackets = re.search(r"\[(.*?)\]", arg)

        if curly_braces is None:
            if brackets is None:
                return [i.strip(",") for i in split(arg)]
            else:
                lexer = split(arg[:brackets.span()[0]])
                retl = [i.strip(",") for i in lexer]
                retl.append(brackets.group())
                return retl
        else:
            lexer = split(arg[:curly_braces.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(curly_braces.group())
            return retl

    def check_args(self, args):
        """checks if args is valid

        Args:
            args (str): the string containing the arguments
            passed to a command

        Returns:
            Error message if args is None or not a valid class,
            else the arguments
        """
        arg_list = self.parse(args)

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.objects:
            print("** class doesn't exist **")
        else:
            return arg_list

    def default(self, param):
        """Default method"""

        cmds = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "count": self.do_count,
                "create": self.do_create
                }

        match = re.search(r"\.", param)
        if match:
            arg1 = [param[:match.span()[0]], param[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in cmds:
                    call = "{} {}".format(arg1[0], command[1])
                    return cmds[command[0]](call)

        print("*** Unknown syntax: {}".format(param))

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
        args = self.check_args(line)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, params):
        """Print instance representation

        Description:
            This method prints the string representation of an instance
            based on the class name and the id. It splits the elements
            in the args parameter into a list. It then assigns the list
            elements to named variables with which will be used to
            fetch instance data

        """

        args = self.check_args(params)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

    def do_destroy(self, params):
        """Delete an instance

        Description:
            This method deletes an instance based on the class name
            and the id. It implements the same approach as the do_show,
            deletes an instance by its id and updates the file with the
            save() method from the file storage class
        """

        arg_list = self.check_args(params)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, params):
        """Print all instances

        Description:
            This method prints all string representation of
            instances either based on the instance name or not.
        """
        arg_list = split(params)
        objects = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in HBNBCommand.objects:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def do_update(self, params):
        """Update an instance

        Description:
            This method updates an instance of a model based on the
            class name and id. Usuage:

            update <class name> <id> <attribute name> "<attribute value>
        """

        arg_list = self.check_args(params)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")

            self.storage.save()

    def do_count(self, param):
        """Count objects

        Description:
            This method counts for the number of instances of a
            class
        """

        values = param.split()
        count = 0

        if len(values) > 0:
            for obj in self.storage.all():
                if obj.startswith(values[0]):
                    count += 1

            print(count)

#   ======================================================================


if __name__ == "__main__":
    HBNBCommand().cmdloop()
