import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

pw_ptr = r"(\d)-(\d) ([a-zA-Z]): (\w+)"

def data_parse(raw):
    return [re.match(pw_ptr, line).groups() for line in raw.split("\n")]


def one(raw):
    passwords = data_parse(raw)

    count = 0
    for i,j,char,pw in passwords:
        c = pw.count(char)

        if int(i) <= c <= int(j):
            count += 1
    return count


def two(raw):
    passwords = data_parse(raw)

    count = 0
    for i,j,char,pw in passwords:
        if pw[int(i)-1] == char ^ pw[int(j)-1] == char:
            count += 1
    
    return count