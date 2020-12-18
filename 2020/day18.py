import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def parse_ops(line):

    cur_str = ""
    depth = 0
    ops = []
    for char in line:

        if char == "(":
            if depth == 0:
                cur_str.strip()
                if len(cur_str) != 0:
                    ops.append(cur_str)
                cur_str=""
            else:
                cur_str += char
            depth +=1
        elif char == ")":
            depth -= 1
            if depth == 0:
                ops.append(parse_ops(cur_str))
                cur_str = ""
            else:
                cur_str += char
        else:
            cur_str += char
    if len(cur_str.strip()) != 0:
        ops.append(cur_str.strip())
    return ops

def operate(ops,sepop="+"):
    ans = 0
    for i in range(len(ops)):
        if type(ops[i]) == list:
            ops[i] = str(operate2(ops[i],sepop))
    ev = (" ".join(ops)).split(sepop)
    for i in range(len(ev)):
        ev[i] = eval(ev[i])
    return math.prod(ev)

def one(raw):
    return sum(operate(parse_ops(line),"+") for line in raw.split("\n"))

def two(raw):
    return sum(operate(parse_ops(line),"*") for line in raw.split("\n"))