import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def data_parse(raw):
    data = raw.splitlines()
    return data


def one(raw):
    data = data_parse(raw)

    a,b =0,0

    for line in data:
        fa,fb = False,False
        for char in set(line):
            if line.count(char) == 2 and not fa:
                a+=1
                fa = True
            elif line.count(char) == 3 and not fb:
                b+=1
                fb = True

    return a*b

def two(raw):
    # raw = test
    data = data_parse(raw)

    for str1, str2 in itertools.combinations(data,2):
        c = set()
        for i, chars in enumerate(zip(str1,str2)):
            if chars[0] != chars[1]: 
                c.add(i)
        
        if len(c) == 1:
            return str1[:i]+str1[i+1:]
            