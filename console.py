#!/usr/bin/python3
"""
HBNB CLONE
"""

from models.base_model import BaseModel 
from models import storage
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    class hbnb
    """
    intro = ''
    prompt = '(hbnb) '
    file = None
    classes = ["BaseModel", "Class"]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        self.close()
        quit()
        return True 

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        self.close()
        return True
    def emptyline(self):
        pass

    
    def do_create(self, arg):
        """
        create  a new instnce of base model
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval("{}()".format(args[0]))
            new_instance.save()
            print(new_instance.id)




    # ----- record and playback -----
    def close(self):
        if self.file:
            self.file.close()
            self.file = None




if __name__ == '__main__':
    HBNBCommand().cmdloop()
