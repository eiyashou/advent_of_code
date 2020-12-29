#!/usr/var/env python3.9

import testfunc as aux
from intcode import *
from collections import defaultdict
import sys

asciistr2str = lambda n : "".join(map(chr,n))
ascii2char = lambda n : chr(n)

def parse(raw):
    return IntCodeMachine(raw, 10000)

def one(bot):
    bot.reset(CLEAR_INPUT, CLEAR_OUTPUT)
    bot.run(HALT_ON_LACKING_FEED)

    maze = dict()
    x=0
    y=0
    while bot.out:
        i = bot.pop()
        if i == 10:
            x=0
            y+=1
        else:
            maze[x,y]=i
            x+=1
    
    res = 0
    for xy,i in filter(lambda n : n[1]==35, maze.items()):
        x,y = xy
        if all(maze.get((x+dx,y+dy), 0)==35 for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))):
            res += x*y
    return res


def two(bot): # TODO: day17year2019
    bot.reset(CLEAR_INPUT, CLEAR_OUTPUT)
    bot[0] = 2

    ROUTINE = ""
    FUNC_A  = ""
    FUNC_B  = ""
    FUNC_C  = ""
    return

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)