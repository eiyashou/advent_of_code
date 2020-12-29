#!/usr/var/env python3.9

import testfunc as aux
import sys, re
from collections import defaultdict

def parse(data):
    res = defaultdict(list)
    for line in data.split("\n"):
        p = re.match(r"^(\w+ \w+) bags contain ([\w, ]+).$",line)
        for k in list(re.finditer(r"(no other bag|(\d+) (\w+ \w+) bag)",p.group(2))):
            if k.group(2) != "":
                res[p.group(1)].append((int(k.group(2)), k.group(3)))
        
    return res


def one(bags):
    
    def parent_bags(child_bags):
        res = []
        for _, bag in child_bags:
            res+=parent_bags(bags[bag]) + [bag]
        return res

    total_bags = parent_bags(tuple(bags["shiny gold"]))
    
    return len(set(total_bags))


def two(data):
    
    def recursive(child_bags, count=1):
        res = 1
        for i, bag in child_bags:
            res+= recursive(data[bag], i)
        return res*count

    return recursive(data["shiny gold"]))-1

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)