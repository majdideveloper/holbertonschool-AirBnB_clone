#!/usr/bin/python3
"""
uinitest for the base moodel
"""

import unittest
import uuid
from datetime import datetime

from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    """
    calss Test 
    """

    def test_id(self):
        """test the id"""
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)

if __name__ =='__main__':
    unittest.main()
