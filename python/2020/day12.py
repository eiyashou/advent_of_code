import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

class Vector:

    def __init__(self, x,y):
        self.x=x
        self.y=y
    
    def __add__(self,o):
        return Vector(self.x+o.x,self.y+o.y)
    
    def __rmul__(self,o):
        return Vector(self.x*o,self.y*o)
    
    def __lmul__(self,o):
        return Vector(self.x*o,self.y*o)
    
    def rotate(self,d):
        d%=360;x=self.x;y=self.y
        for _ in range(d//90):
            x, y = -y, x
        
        return Vector(x,y)

def data_parse(raw):
    data = [(p[0], int(p[1:])) for p in raw.split("\n")]
    return data


DIR = {"N":Vector(0,1), "S":Vector(0,-1), "E":Vector(1,0),"W":Vector(-1,0)}

def one(raw):
    # raw = test
    data = data_parse(raw)

    ptr = Vector(1,0)
    p = Vector(0,0)

    for d, v in data:

        if d == "L": ptr.rotate(v)
        elif d == "R": ptr.rotate(-v)
        elif d == "F": p += v*ptr
        else: p += v*DIR[d]

    return abs(p)


def two(raw):
    # raw = test
    data = data_parse(raw)

    p = Vector(0,0)
    wp = Vector(10,1)

    for d, v in data:

        if d == "L": wp = wp.rotate(v)
        elif d == "R": wp = wp.rotate(-v)
        elif d == "F": p += v*wp
        else: wp += v*DIR[d]

    return abs(p)


test = """
"""