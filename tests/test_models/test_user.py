#!/usr/bin/python3
"""
uinitest for the User
"""



from models.user import User
from datetime import datetime
from time import sleep
import unittest
import uuid

class Test_User(unittest.TestCase):
    """
    calss Test for User 
    """
    def test_user(self):
        c_user = User()
        c_user.email = "hana"
        msg = "hana"
        self.assertTrue(c_user.email, msg)
