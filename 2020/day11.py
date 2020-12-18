import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

class Tile():

    def __init__(self, state):
        self.neighbours = []
        self.sit = state
    
    def __getitem__(self, k):
        return self.neighbours[k]

    def copy(self):
        return Tile(self.sit)
    
class Map():

    def __init__(self, nodes, w, h):
        self.w = w
        self.h = h
        self.nodes = nodes
    
    def __getitem__(self, s):
        if type(s) == tuple and len(s) == 2:
            x,y = s
            return self.nodes[x+y*self.w]
        else:
            raise IndexError()
    
    def __eq__(self, o):
        for r1, r2 in zip(self.nodes, o.nodes):
            if r1.sit != r2.sit:
                return False
        return True

    def __str__(self):
        res = ""
        for i, n in enumerate(self.nodes):
            res += n.sit
            if i%self.w == self.w-1:
                res += "\n"
        
        return res[:-1]
    
    def convolute(self, x, y, depth_=1, tolerance=4):

        count = 0
        temp = None
        n = self[x,y]

        for i in range(8):
            temp = n
            depth = depth_
            while depth > 0 and temp != None:
                temp = temp[i]
                if temp != None and temp.sit != ".":
                    count += 1 if temp.sit == "#" else 0
                    break
                depth -= 1
        
        if n.sit == "L" and count == 0:
            return "#"

        elif n.sit == "#" and count >= tolerance:
            return "L"
        
        else: 
            return n.sit

def data_parse(raw):
    W = len(raw.split("\n",2)[0])
    H = raw.count("\n")+1

    map_1 = Map([Tile(char) for char in raw.replace("\n","")], W, H)
    map_2 = Map([t.copy() for t in map_1.nodes], W, H)

    for i,j in aux.range_2D(W,H):
        for dx, dy in aux.eight_dir():
            x = i+dx
            y = j+dy

            if 0 <= x < W and 0 <= y < H: 
                map_1[i, j].neighbours.append(map_1[x, y])
                map_2[i, j].neighbours.append(map_2[x, y])
            else:
                map_1[i, j].neighbours.append(None)
                map_2[i, j].neighbours.append(None)

    return map_1, map_2

def one(raw):
    map_1, map_2 = data_parse(raw)
    n = 0

    while True:
   
        for i,j in aux.range_2D(map_1.w,map_1.h):
            if map_1[i,j].sit == ".":
                continue
            map_2[i,j].sit = map_1.convolute(i,j, 1, 4)
        
        if map_1 == map_2:
            break

        map_1, map_2 = map_2, map_1
        n += 1 
        print(n)

    return sum(1 for t in map_2.nodes if t.sit == "#")

def two(raw):
    map_1, map_2 = data_parse(raw)
    n = 0

    while True:
   
        for i,j in aux.range_2D(map_1.w,map_1.h):
            if map_1[i,j].sit == ".":
                continue
            map_2[i,j].sit = map_1.convolute(i,j, 999, 5)
        
        if map_1 == map_2:
            break

        map_1, map_2 = map_2, map_1
        n += 1 
        print(n)

    return sum(1 for t in map_2.nodes if t.sit == "#")