import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

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

def one(R):
    return sum(checks["valid"](F) for f in R.split("\n\n")if(F:=f.replace("\n"," ").split(" ")))

def two(raw):
    passports = [{D[:3]:D[4:].strip()} for d in raw.split("\n\n") for D in d.replace("\n"," ").split()]
    return sum(checks["valid"](p) and all(checks[k](v) for k,v in p.items()) for p in passports)