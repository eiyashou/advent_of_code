import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

bit36_format = lambda x : "{0:036b}".format(int(x))

def data_parse(raw):
    data = []
    for line in raw.splitlines():
        if bool(p := re.fullmatch(r"mask = ([X10]+)", line)):
            data.append((p.group(1),))
        elif bool(p := re.fullmatch(r"mem\[(\d+)\] = (\d+)", line)):
            data.append((bit36_format(p.group(1)), bit36_format(p.group(2))))
    return data


def apply_mask(data, func):
    mask = ["0" for _ in range(36)]
    mem = {}
    for line in data:
        if len(line) == 1:
            mask = line[0]
        else:
            func(mem, line)
    return sum(int(v, 2) for v in mem.values())


def one(raw):
    data = data_parse(raw)

    def x(mem,line):
        mem[line[0]] = ""
        for bit, msk in zip(line[1], mask):
            if msk == "X": mem[line[0]] += bit
            else: mem[line[0]] += msk

    return apply_mask(data, x)


def two(raw):
    data = data_parse(raw)

    def x(mem,line):
        temp_adr = ""
        for bit, msk in zip(line[0], mask):
            if msk in "1X": temp_adr += msk
            else: temp_adr += bit

        count_x = mask.count("X")-1
        for i in range(2**count_x):
            adr = str(temp_adr)
            for c in range(count_x, -1, -1):
                adr.replace("X", str((i//(2**c))%2), 1)
            mem[adr] = line[1]

    return apply_mask(data, x)