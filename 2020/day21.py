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
    
    while food:
        decided_alrgn = [k for k,v in food.items() if len(v) == 1][0]
        ingrd = food[decided_alrgn].pop()

        occupied[ingrd] = decided_alrgn
        del food[decided_alrgn]
        for k,v in food.items():
            food[k].discard(ingrd)
    
    return all_ingreds, occupied

def one(raw):
    all_ingreds, pairs = parse_data(raw)
    
    ingrd_count = Counter(all_ingreds)
    return sum(v for k,v in ingrd_count.items() if k not in pairs)

def two(raw):
    occupied = parse_data(raw)[1]
    
    return ','.join(sorted(occupied.keys(), key=lambda x: occupied[x]))

