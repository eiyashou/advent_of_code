from collections import defaultdict, Counter
import re
from libs.aux_funcs import Queue # Queue is just a normal queue with a few extra features that help me during debugging

def parse_data(raw):
    food = defaultdict(set)
    all_ingreds = []

    for line in raw.splitlines():
        parts = re.match(r"(.+) \(contains (.+)\)", line).groups()
        ingrds = set(parts[0].split())
        alrgns = set(parts[1].split(", "))

        all_ingreds.extend(ingrds)
        for alrgn in alrgns:
            food[alrgn] = food[alrgn]&ingrds if food[alrgn] else food[alrgn]|ingrds
    
    occupied = dict()
    Q = Queue(sorted(food.items(), key = lambda x : len(x[1])))

    while Q:
        alrgn, ingrds = Q.pop()
        ingrds = ingrds - set(occupied.keys())
        if len(ingrds) == 1: 
            occupied[ingrds.pop()] = alrgn
            if Q: Q = Queue(sorted(Q, key = lambda x : len(x[1])))
            else: return occupied, all_ingreds
        else: Q.append(alrgn, ingrds)

def one(raw):
    pairs, all_ingreds = parse_data(raw)
    ingrd_count = Counter(all_ingreds)
    return sum(v for k,v in ingrd_count.items() if k not in pairs)

def two(raw):
    occupied = parse_data(raw)[0]
    return ','.join(sorted(occupied.keys(), key=lambda x: occupied[x]))

