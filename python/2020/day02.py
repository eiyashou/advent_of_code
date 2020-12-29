#!/usr/var/env python3.9

import testfunc as aux
import sys, re

pw_ptr = re.compile(r"(\d)-(\d) ([a-zA-Z]): (\w+)")
def data_parse(raw):
    return [pw_ptr.fullmatch(line).groups() for line in raw.split("\n")]

def one(data):
    return sum((int(i) <= pw.count(char) <= int(j) for i,j,char,pw in data))

def two(data):
    return sum(( (pw[int(i)] == c) ^ (pw[int(j)] == c) for i,j,char,pw in data if (PW:="."+pw)))

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)