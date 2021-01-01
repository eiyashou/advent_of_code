#!/usr/var/env python3.9

import testfunc as aux
import sys, re
from collections import defaultdict

def parse(raw):
    transforms, molecule = raw.split("\n\n")
    dict_trans = defaultdict(list)
    for mol, trans in map(lambda n : re.match("(\w+) => (\w+)", n).groups(), transforms.split("\n")):
        dict_trans[mol].append(trans)
    return dict_trans, molecule

def one(data):
    transforms, molecule = data
    seen = set()

    for mol, trans in transforms.items():
        cParts = molecule.count(mol)-1
        parts = molecule.replace(mol,"{}")
        
        for i in range(cParts+1):
            for t in trans:
                res = parts.format(*(([mol]*(i)) + [t] + ([mol]*(cParts-i))))
                seen.add(res)

    return len(seen)

def two(data):
    transforms, molecule = data
    rev_transforms = defaultdict(list)

    for k,v in transforms.items():
        for trans in v:
            rev_transforms[trans].append(k)

    res = 0
    transforms = sorted(rev_transforms.items(), reverse=True,key = lambda n : len(n[0]))
    
    print(transforms)
    print(all(map(lambda n : len(n[1]) == 1, transforms)))
    while True:
        prev_molecule = molecule
        for trans,now in transforms:
            res += molecule.count(trans)
            molecule = molecule.replace(trans, k) 
            print(molecule)
        
        if prev_molecule == molecule:
            break
    return res-1

test_thing = """e => H
e => O
H => HO
H => OH
O => HH

HOH"""

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)