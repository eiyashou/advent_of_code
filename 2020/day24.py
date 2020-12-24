#!/usr/bin/env python

import libs.aux_funcs as aux
from collections import Counter
import re

class V:

    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self,o):
        return V(self.x+o.x, self.y+o.y, self.z+o.z)
    
    def __radd__(self, o):
        if isinstance(o, int):
            return self
        else:
            return self.__add__(o)
    
    def __call__(self):
        return (self.x, self.y, self.z)


hex2threedee = {
    "e": V(1,-1,0),
    "ne": V(1,0,-1),
    "nw": V(0,1,-1),
    "w": V(-1,1,0),
    "sw": V(-1,0,1),
    "se": V(0,-1,1)
}

with open("data/aoc/inputs/2020/day24.txt", "r") as f:
    raw = f.read()

def parse(raw):
    data=[]
    for line in raw.splitlines():
        row = []
        for p in re.findall(r"(e|w|nw|ne|se|sw)", line):
            row.append(hex2threedee[p])
        data.append(row)

    return data


def one(data):
    black = set()
    for line in data:
        final = sum(line)()
        if final in black: black.remove(final)
        else: black.add(final)
    return len(black)

def two(data):

    black = set()
    for line in data:
        final = sum(line)()
        if final in black: black.remove(final)
        else: black.add(final)

    adj = list(v() for v in hex2threedee.values())
    for _ in range(1,100+1):
        neighbours = Counter(tuple(a+b for a,b in zip(v,dV)) for v in black for dV in adj)
        black = {k for k in neighbours if neighbours[k] == 2 or (k in black and neighbours[k] ==1)}

    return len(black)