#!/usr/var/env python3.9

import testfunc as aux
import sys, re

checks = {
    "valid": lambda n : len(n)==8 or (len(n)==7 and 'cid' not in n)
    "byr": lambda n : 1920<= int(n) <=2002,
    "iyr": lambda n : 2010<= int(n) <=2020,
    "eyr": lambda n : 2020<= int(n) <=2030,
    "hgt": lambda n : bool(p:=re.fullmatch(r"(\d+)(cm|in)", n)) and checks[p.group(2)](p.group(1)),
    "hcl": lambda n : bool(re.fullmatch(r"#[0-9a-f]{6}", n)),
    "ecl": lambda n : n in {"amb","blu","brn","gry","grn","hzl","oth"},
    "pid": lambda n : bool(re.fullmatch(r"(\d){9}", n)),
    "cm" : lambda n : 150<= int(n) <=193,
    "in" : lambda n : 59<= int(n) <=76
}

def parse(raw):
    return [{D[:3]:D[4:].strip()} for d in raw.split("\n\n") for D in d.replace("\n"," ").split()]

def one(data):
    return sum(map(checks["valid"], data))

def two(data):
    return sum((checks["valid"](p) and all(checks[k](v) for k,v in p.items()) for p in data))

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)