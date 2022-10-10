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
    
    def test_save(self):
        """
        test save 
        """
        save1 = BaseModel()
        save2 = BaseModel()
        self.assertEqual(save1.save(), save2.save())
        

if __name__ =='__main__':
    unittest.main()
