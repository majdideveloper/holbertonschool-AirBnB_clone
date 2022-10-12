#!/usr/bin/python3
"""
uinitest for the User
"""

import unittest
import uuid
from datetime import datetime
from time import sleep

from models.base_model import BaseModel

class Test_User(unittest.TestCase):
    """
    calss Test for User 
    """
    def inst_user(self):
        c_user = User()
        c_user.email = "5002@holbertonstudents.com"
        c_user.password ="passWord"
        c_user.first_name ="Hana"
        c_user.last_name = "Ouerghemmi"
