#!/usr/bin/python3
"""Command line interface implementation"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class for command line interface"""

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


#   ======================================================================

if __name__ == "__main__":
    HBNBCommand().cmdloop()
