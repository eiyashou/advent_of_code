#!/usr/bin/env python

import libs.aux_funcs as aux
from pathfinding import *

# TODO: y2019d20

class Gate:

    def __init__(self):
        pass


with open(f"data/aoc/inputs/2019/day20.txt", "r") as f:
    raw = f.read()

    grid = None
    gates = {"AA":Gate}

    # All cells which are portals
    # In here we entangle the portals:tm:
    for pos, cell in filter(lambda n : n[1].c != "." and  any(a.c == "." for a in n[1].adj.values()), grid.map.items()):
        

        
        """
        for 
        if adj.c == "A" and adj[d].c == "A":
            self.start = cell.adj[d] = adj
        elif adj.c == "Z" and adj[d].c == "Z":
            self.end = cell.adj[d] = adj
        elif adj.c != "." and adj[d].c != ".":
            gate = Gate()
            self.gates[key] = cell.adj[d] = gate
        else:"""

def one(data):
    return


def two(data):
    return


if __name__=="__main__":
    aux.timeit(one, parse(raw))
    #aux.timeit(two, parse(raw))