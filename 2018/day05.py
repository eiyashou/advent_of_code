import sys, os, re, math, hashlib, itertools, functools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def one(raw):

    chem = ""
    for c in raw:
        chem = chem[:-1] if chem != "" and chem[-1] != c and chem[-1].upper() == c.upper() else c

    return len(chem)
    
def one_line(R):
    l="";[(l:=l[:-1]if l!=""and l[-1]!=c and l[-1].upper()==c.upper()else c)for c in R];return len(l)

def two(raw):

    minimum = None
    
    for ele in set(x.lower() for x in R):
        
        raw_r = R.replace(ele,"").replace(ele.upper(),"")
        chem = ""

        for c in raw_r:
            chem = chem[:-1] if chem != "" and chem[-1] != c and chem[-1].upper() == c.upper() else c
        
        if minimum == None or minimum > len(chem):
            minimum = len(chem)

    return minimum

def two_line(R):
    return min([(l:=0),[(l:=l[:-1]if l!=""and l[-1]!=c and l[-1].upper()==c.upper()else c)for c in R.replace(e,"").replace(e.upper(),"")],len(l)][-1]for e in set(x.lower()for x in R))