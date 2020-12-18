import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

def data_parse(data):
    res = defaultdict(list)
    
    for line in data.split("\n"):
        try:
            p = re.match(r"^(\w+ \w+) bags contain ([\w, ]+).$",line)

            for k in list(re.finditer(r"(no other bag|(\d+) (\w+ \w+) bag)",p.group(2))):
                if k.group(2) != "":
                    res[p.group(1)].append((int(k.group(2)), k.group(3)))
        
    return res


def one(raw, your_bag = "shiny gold"):
    bags = data_parse_one(raw) #the laws the bags must follow
    
    def parent_bags(child_bags):
        res = []

        for _, bag in child_bags:
            res+=parent_bags(bags[bag]) + [bag]
    
        return res

    total_bags = parent_bags(tuple(bags[your_bag]))
    
    return len(set(total_bags))


def two(raw, your_bag = "shiny gold"):
    dic = data_parse_two(raw)
    
    def recursive(child_bags, count=1):
        res = 1
        
        for i, bag in child_bags:
            res+= recursive(dic[bag], i)
        
        return res*count

    return recursive(dic[your_bag]))-1