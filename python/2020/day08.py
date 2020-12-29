#!/usr/var/env python3.9

import testfunc as aux
import sys

def parse(data):
    return [[n, int(p) for n,p in x.split(" ")] for x in data.split("\n")]

def one(data, pop=False):
    acc = 0
    pc = 0
    visited = []
    
    while pc not in visited or pc < len(data):
            
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

def two(Script):
    
    fails = part_one(data, True)
    
    for fail in fails:
        
        script = Script.copy()    
        
        if script[fail][0] in {"jmp", "nop"}:
            script[fail][0] = "jmp" if cmd == "nop" else "nop"
        else: continue
            
        acc = 0
        pc = 0
        visited = []
        
        while pc not in visited:

            if pc >= len(script):
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

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)