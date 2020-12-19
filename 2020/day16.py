import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np



def data_parse(raw):
    frags = raw.split("\n\n")
    
    fields = {p.group(1):(lambda n : int(p.group(2)) <= n <= int(p.group(3)) or int(p.group(4)) <= n <= int(p.group(5))) 
                for line in frags[0].split("\n") 
                if (p:=re.fullmatch(r"([\w ]+)\: (\d+)-(\d+) or (\d+)-(\d+)",line))}

    my_ticket = [int(x) for x in frags[1].split("\n")[1].split(",")]
    
    other_tickets = [[int(x) for x in line.split(",")] for line in frags[2].split("\n")[1:]]

    return fields, my_ticket, other_tickets


def one(raw):
    fields, _, other_tickets = data_parse(raw)
    rangs = fields.values()
    L_ticket = len(other_tickets[0])

    err = 0
    for ticket in other_tickets:
        valid = [False for _ in range(L_ticket)]

        for i, x in enumerate(ticket):
            for f in rangs:
                if f(x):
                    break
            else:
                err += x
    
    return err


def two(raw):
    fields, my_ticket, other_tickets= data_parse(raw)

    rangs = fields.value()
    valid_tickets = []
    for ticket in other_tickets:
        for field in ticket:
            for field_check in rangs:
                if field_check(field):
                    break
            else:
                break
        else:
            valid_tickets.append(ticket)

    columns = zip(*valid_tickets)
    Q = fields.items()
    options = {i:{k for cell in column for k,f in Q if f(cell)} for i,column in enuemrate(columns)}
    
    Q = options.items()
    columns = [None]*len(my_ticket)
    while Q:
        pos, options = Q.pop(0)
        opts = {z for z in options if z not in columns}

        if len(options) == 1: columns[pos] = options.pop()
        else: Q.append((pos,opts))

    return math.prod(v for k,v in zip(columns, my_ticket) if k.startswith('departure'))

def two_sys(raw):
    fields, my_ticket, other_tickets= data_parse(raw)

    rangs = fields.value()
    valid_tickets = []
    for ticket in other_tickets:
        for x in ticket:
            for f in rangs:
                if f(x):
                    break
            else:
                break
        else:
            valid_tickets.append(ticket)

    columns = zip(*valid_tickets)
    candidates = [[int(all(f(cell) for cell in column)) for column in columns] for f in fields.values()]

    #TODO: algebra solution to 2020-16-p2

    columns = list(fields.keys())
    return math.prod(v for k,v in zip(res, my_ticket) if columns[k].startswith('departure'))