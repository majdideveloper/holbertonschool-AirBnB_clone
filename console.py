#!/usr/bin/python3
"""
HBNB CLONE
"""

from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models import storage
import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """
    class hbnb Command
    """
    intro = ''
    prompt = '(hbnb) '
    file = None
    classes = ["BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"]

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
            if not item_print:
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
            """obj = "{}.{}".format(args[0], args[1])
            if obj in storage.all():
                storage.all().pop(obj)
                storage.save()"""
            obj = "{}.{}".format(args[0], args[1])
            all_obj = storage.all()
            delete_item = False
            for k in all_obj.keys():
                if obj == k:
                    delete_item = True
            if delete_item:
                del all_obj[obj]
                storage.save()
            else:
                print("** no instance found **")

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
                    print(str_list)
                elif len(args) == 0:
                    str_list.append(v.__str__())
                    print(str_list)
                else:
                    print("** no instance found **")

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
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) > 4:
            return
        else:
            obj = "{}.{}".format(args[0], args[1])
            all_obj = storage.all()
            update_item = False
            for k, v in all_obj.items():
                if obj == k:
                    update_item = True
                    setattr(all_obj[obj], args[2], args[3])
            if update_item:
                """
                    new_dict = v.to_dict()
                    print(type(new_dict))
                    new_dict[args[2]] = args[3]
                    print(new_dict)
                    new_dict = BaseModel(new_dict)
                    bint(new_dict)
                    models.storage.save()

                """
                #my_new_obj= all_obj[obj]
                #my_new_obj.updated_at = datetime.now()
                storage.save()
            else:
                print("** no instance found **")

    # ----- record and playback -----
    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
