import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def data_parse(data):
    return [[n, int(p) for n,p in x.split(" ")] for x in data.split("\n")]

def one(raw, pop=False):
    data = data_parse(raw)
    L = len(data)

    acc = 0
    pc = 0
    visited = []
    
    while pc not in visited or pc < L:
            
        visited.append(pc)
        
        cmd, val = data[pc]
        
        if cmd == "acc":
            acc += val
            pc += 1
        elif cmd == "jmp":
            pc += val
        elif cmd == "nop":
            pc += 1
        
    if pop:
        return visited[visited.index(pc):]
    else: 
        return acc

def two(raw):
    script = data_parse(raw)    
    L = len(Script)
    
    fails = part_one(raw, True)
    
    for fail in fails:
        
        script = Script.copy()    
        
        if script[fail][0] in {"jmp", "nop"}:
            script[fail][0] = "jmp" if cmd == "nop" else "nop"
        else: continue
            
        acc = 0
        pc = 0
        visited = []
        
        while pc not in visited:

            if pc >= L:
                return acc
                
            visited.append(pc)
            
            cmd, val = data[pc]
            
            if cmd == "acc":
                acc += val
                pc += 1
            elif cmd == "jmp":
                pc += val
            elif cmd == "nop":
                pc += 1