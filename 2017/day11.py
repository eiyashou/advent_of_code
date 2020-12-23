#!/usr/bin/env python

class V:

    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self,o):
        return V(self.x+o.x, self.y+o.y, self.z+o.z)
    
    def __abs__(self):
        return max((abs(self.x),abs(self.y),abs(self.z)))


hex2threedee = {
    "n": V(1,0,-1),
    "ne": V(0,1,-1),
    "se": V(-1,1,0),
    "s": V(-1,0,1),
    "sw": V(0,-1,1),
    "nw": V(1,-1,0)
}

def parse(raw):
    data=list(map(lambda n : hex2threedee[n], raw.split(",")))
    return data


def one(data):
    final = V()
    for v in data:
        final += v
    return final


def two(data):
    final = V()
    maximum = 0
    for v in data:
        final += v
        m = abs(final)
        if m > maximum:
            maximum = m
    return maximum