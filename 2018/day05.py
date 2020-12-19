import sys, os, re, math, hashlib, itertools, functools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

sample='''X'''

def one(raw):

    chem = raw[0]
    
    for c in raw[1:]:

        if chem != "" and chem[-1] != c and chem[-1].upper() == c.upper():
            changes = True
            chem = chem[:-1]
        else:
            chem += c

    return len(chem)
    
def two(R):

    minimum = None
    
    for ele in set(x.lower() for x in R):
        
        raw = R.replace(ele,"").replace(ele.upper(),"")
        chem = ""
        
        for c in raw:

            if chem != "" and chem[-1] != c and chem[-1].upper() == c.upper():
                changes = True
                chem = chem[:-1]
            else:
                chem += c
        
        if minimum == None or minimum > len(chem):
            minimum = len(chem)

    return minimum