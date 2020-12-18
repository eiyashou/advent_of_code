import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def hyperconway(raw, G=100,N=2):    
    if N < 2 or G < 1: raise ValueError()
    
    adj_coords = list(filter(any, itertools.product((-1, 0, 1), repeat=N)))
    m1 = {(i,j,*([0]*(N-2))) for j,y in enumerate(raw.split("\n")) for i,x in enumerate(y) if x == "#"}
    print(f"Gen 0, count={len(m1)}")

    for g in range(1,G+1):
        neighbours = Counter(tuple(v+dv for v,dv in zip(V,dV)) for dV in adj_coords for V in m1)
        m1={p for p in neighbours if neighbours[p]==3 or (p in m1 and neighbours[p]==2)}
        print(f"Gen {g}, count={len(m1)}")

    return len(m1)

def one(raw):
    return hyperconway(raw,G=6,N=3)

def two(raw):
    return hyperconway(raw,G=6,N=4)