import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np



def data_parse(raw):
    data = [int(x) for x in raw.split(",")]
    return data

def say_game(start, n=2020):
    said = {num:i+1 for i,num in enumerate(start)}
    L = len(start)
    say = start[-1]

    for i in range(L, n):

        if say not in said:
            said[say] = i
            say = 0
        else:
            nxt = i-said[say]
            said[say] = i
            say = nxt
        
        print(i+1, say, said)

    return say

def one(raw):
    start = data_parse(raw)
    return say_game(start, 2020)

def two(raw):
    start = data_parse(raw)
    return say_game(start, 30000000)