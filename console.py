#!/usr/bin/python3
"""
HBNB CLONE
"""

import cmd



class HBNBCommand(cmd.Cmd):
    """

    """
    intro = ''
    prompt = '(hbnb) '
    file = None

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

    # ----- record and playback -----
    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
