#!/usr/var/env python3.9

import testfunc as aux
import sys
from collections import defaultdict
from intcode import *
import time, os, sys

def parse(raw):
    return IntCodeMachine(raw, 3000)

id2tile=["   ", "███","###", "---", "(o)"]
    
def one(bot):
    bot.reset(CLEAR_OUTPUT,CLEAR_OUTPUT)
    tiles = defaultdict(int)

    bot.run(halt_on=3)
    while not bot.done():
        x,y,i = (bot.pop() for _ in range(3))
        tiles[x,y]=i
        bot.run(halt_on=3)

    return len(tiles)

def two(bot):
    bot.reset(CLEAR_INPUT,CLEAR_OUTPUT)
    bot[0] = 2
    tiles = defaultdict(int)
    score = 0
    prev_cur = 0

    while not bot.done():
        bot.run(HALT_ON_LACKING_FEED,halt_on=3)
        while not bot.needs_input() and not bot.done():
            x,y,i = (bot.pop() for _ in range(3))
            if x == -1:
                score = i
            else:
                tiles[x,y]=i
            bot.run(HALT_ON_LACKING_FEED,halt_on=3)
        
        if not bot.done():            
            ball = set(filter(lambda n : n[1] == 4, tiles.items())).pop()[0]
            cursor = set(filter(lambda n : n[1] == 3, tiles.items())).pop()[0]

            xb, xc = ball[0], cursor[0]

            if ball[1]+1 == cursor[1] and xb == xc:
                dir_ = (prev:=0)
            elif xb > xc:
                dir_ = (prev:= 1)
            elif xb < xc:
                dir_ = (prev:=-1)
            else:
                dir_ = -prev

            bot << dir_

    return score

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)