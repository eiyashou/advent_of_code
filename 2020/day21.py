from collections import defaultdict, Counter
import re

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
    Q = list(food.items())

    while Q:
        alrgn, ingrds = Q.pop(0)
        ingrds = ingrds - set(occupied.keys())
        if len(ingrds) == 1: occupied[ingrds.pop()] = alrgn
        else: Q.append((alrgn, ingrds))
    
    return occupied, all_ingreds

def one(raw):
    pairs, all_ingreds = parse_data(raw)
    ingrd_count = Counter(all_ingreds)
    return sum(v for k,v in ingrd_count.items() if k not in pairs)

def two(raw):
    occupied = parse_data(raw)[0]
    return ','.join(sorted(occupied.keys(), key=lambda x: occupied[x]))

