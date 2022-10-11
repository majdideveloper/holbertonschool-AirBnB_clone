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
    class hbnb Command
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

    def do_show(self, arg):
        """
        show a new instnce of base model
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            all_obj = storage.all()
            item_print = False
            for k, v in all_obj.items():
                id_obj = k.split('.')[1]
                if id_obj == args[1]:
                    obj = v
                    print(obj)
                    item_print = True
            if item_print == False:
                print("** no instance found **")
            

    def do_destroy(self, arg):
        """
        Delete an instnce of Class Name
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            obj = "{}.{}".format(args[0], args[1])
            if obj in storage.all():
                storage.all().pop(obj)
            else:
                storage.save()

    def do_all(self, arg):
        """
        Print all string represntation of all instance based 
        or not in the class name
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            str_list = []
            for v in storage.all().values():
                if len(args) > 0 and args[0] == v.__class__.__name__:
                    str_list.append(v.__str__())
                elif len(args) == 0:
                    str_list.append(v.__str__())
            print(str_list)
    


    def do_update(self, arg):
        """
        Update an instnce of Class Name
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
   


    # ----- record and playback -----
    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
