#!/usr/var/env python3.9

import testfunc as aux
import sys
from collections import defaultdict
from intcode import *

def parse(raw):
    return IntCodeMachine(raw, 2000)

DIR = [(1,0),(0,-1),(-1,0),(0,1)]

def run_bot(bot, panels):
    bot.reset(CLEAR_INPUT,CLEAR_OUTPUT)
    x,y=0,0
    d=1

    while True:

        data << int(panels[x,y])
        data.run(halt_on=2)

        if len(data.out) < 2:
            break
        
        panels[x,y] = bool(data.pop())
        d = (d+(-1 if data.pop() else 1))%4
        x += DIR[d][0]
        y += DIR[d][1]

def dict_map(maze, pri):

    X,Y = map(lambda n : sorted(set(n)), list(zip(*list(maze.keys()))))

    x1,x2 = X[0], X[-1]
    y1,y2 = Y[0], Y[-1]

    res = ""
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            res += pri(maze[x,y])
        res += "\n"
    return res[:-1]

def one(data):
    panels = defaultdict(lambda : False)
    run_bot(data, panels)
    return len(panels)

def two(data):
    panels = defaultdict(lambda : False)
    panels[0,0]=True
    run_bot(data, panels)
    print()
    print(dict_map(panels, lambda n : "██" if n else "  "))
    print()

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)