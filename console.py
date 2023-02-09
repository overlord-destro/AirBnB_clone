#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """CLass for command line interface"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quits console upon entering of prompt"""
        return True

    def do_EOF(self, line):
        """Exits console upon entering of prompt"""
        return True

    def emptyline(self):
        """
        overrides emptyline method and executes nothing
        when nothing is typed
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if line:
            if line != "BaseModel":
                print("** class doesn't exist **")
            else:
                inst = BaseModel()
                inst.save()
                print(inst.id)
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
