#!/usr/bin/python3
from models.base_model import BaseModel

bm1 = BaseModel()
bm2 = BaseModel()

print(bm1.id," ", bm2.id)
print(bm1.id != bm2.id)

bm3 = BaseModel()
print(bm3.id)
