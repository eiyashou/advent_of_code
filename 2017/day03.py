#!/usr/bin/env python

import itertools

with open(f"data/aoc/inputs/2017/day3.txt", "r") as f:
    raw = f.read()


def parse(raw):
    data=int(raw)
    return data

def square_gen(r):

    for i in range(-r+1,r+1):
        yield r, i
    
    for i in range(r-1,-r-1,-1):
        yield i, r
    
    for i in range(r-1,-r-1,-1):
        yield -r, i
    
    for i in range(-r+1,r+1):
        yield i, -r

def one(data):

    r = 0
    val = 1
    while True: 
        r+=1
        for x,y in square_gen(r):
            val += 1
            if val == data:
                return abs(x)+abs(y)

def two(data):

    grid = {(0,0): 1,(1,0): 1}

    r = 0
    while True:
        
        r+=1
        for x,y in square_gen(r):
            val = sum(grid.get((x+dx, y+dy), 0) for dx,dy in itertools.product((-1,0,1), repeat=2) if any((dx,dy)))
            if val > data:
                return val
            else:
                grid[x,y] = val 