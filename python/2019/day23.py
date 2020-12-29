#!/usr/var/env python3.9

# TODO: repr of day23year2019

import testfunc as aux
import sys
from collections import defaultdict
from intcode import *

def parse(raw):
    network = [IntCodeMachine(raw, mem_length=2500) for _ in range(50)]
    for i,comp in enumerate(network):
        comp << i
    return network

class Packets:

    def __init__(self):
        self.queue = []
    
    def __bool__(self):
        return bool(self.queue)

    def __iter__(self):
        return iter(self.queue)

    def __lshift__(self, o):
        if isinstance(o, deque):
            while o:
                self.append(o.popleft())
        elif isinstance(o, Iterable):
            for e in o:
                self.append(e)
        elif isinstance(o, IntCodeMachine):
            while o.out:
                self.append(o.pop())
        else:
            self.append(o)

    def clear(self):
        self.queue.clear()

    def append(self,x):
        self.queue.append(x)
    
    def pop(self):
        return self.queue.pop(0)

def one(network):

    packets = defaultdict(Packets)

    while 255 not in packets:        
        for adr, comp in enumerate(network):
            while True:
                try:
                    comp.run(halt_on=3)
                except NeedsInput:
                    break
                dest,x,y = (comp.pop() for _ in range(3))
                packets[dest] << (x,y)

        for adr, comp in enumerate(network):
            comp << packets[adr]
            if packets[adr]:
                packets[adr].clear()
            else:
                comp << -1
                

    return packets[255].queue[1]

class NAT:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __lshift__(self, o):
        self.x, self.y = o
    
    def pop(self):
        return (self.x,self.y)

def two(network):
    for i,comp in enumerate(network):
        comp.reset(CLEAR_OUTPUT, CLEAR_INPUT)
        comp << i

    packets = defaultdict(Packets)
    packets[255] = (nat:=NAT())

    prev_y = None

    while True:        
        for adr, comp in enumerate(network):
            while True:
                try:
                    comp.run(halt_on=3)
                except NeedsInput:
                    break
                dest,x,y = (comp.pop() for _ in range(3))
                packets[dest] << (x,y)
        
        idle = True

        for adr, comp in enumerate(network):
            comp << packets[adr]
            if packets[adr]:
                packets[adr].clear()
                idle = False
            else:
                comp << -1

        if idle:
            x,y = nat.pop()

            if prev_y!=None and prev_y == y:
                return y
            
            prev_y=y
            network[0] << (x,y)

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)