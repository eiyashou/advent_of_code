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
        d%=360
        for _ in range(d//90):
            self.x, self.y = -self.y, self.x


def data_parse(raw):
    res = []
    for n in raw.split(","):
        res.append( ( (m:=n.strip())[0], int(m[1:]) ) )
    return res


def one(raw):
    # raw = test
    data = data_parse(raw)
    p = Vector(0,0)
    d = Vector(0,-1)
    for r, n in data:
        d = d.rotate(3 if r == "R" else 1)
        p += n*d

    return abs(p)


def two(raw):
    # raw = test
    data = data_parse(raw)
    p = Vector(0,0)
    d = Vector(0,-1)
    p_vis = {(p.x, p.y)}
    for r, n in data:
        
        d = d.rotate(3 if r == "R" else 1)
        for _ in range(n):
            p += d

            if (p_t := (p.x, p.y)) in p_vis: return abs(p)
            else: p_vis.add(p_t)

    return abs(p)


test = """
"""