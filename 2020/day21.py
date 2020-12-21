from collections import defaultdict
import re

sample='''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''

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
    
    return food, all_ingreds


def one(raw):
    food, all_ingreds = parse_data(raw)

    occupied = dict()

    while food:
        decided_alrgn = [k for k,v in food.items() if len(v) == 1][0]
        ingrd = food[decided_alrgn].pop()

        occupied[ingrd] = decided_alrgn
        del food[decided_alrgn]
        for k,v in food.items():
            food[k].discard(ingrd)
    
    ingrd_count = Counter(all_ingreds)
    return sum(v for k,v in ingrd_count.items() if k not in occupied)

def two(raw):
    food = parse_data(raw)[0]

    for line in raw.splitlines():
        parts = re.match(r"(.+) \(contains (.+)\)", line).groups()
        ingrds = set(parts[0].split())
        alrgns = set(parts[1].split(", "))

        for alrgn in alrgns:
            food[alrgn] = food[alrgn] & ingrds if food[alrgn] else food[alrgn] | ingrds

    occupied = dict()
    
    while food:
        decided_alrgn = [k for k,v in food.items() if len(v) == 1][0]
        ingrd = food[decided_alrgn].pop()

        occupied[ingrd] = decided_alrgn
        del food[decided_alrgn]
        for k,v in food.items():
            food[k].discard(ingrd)
    
    return ','.join(sorted(occupied.keys(), key=lambda x: occupied[x]))

