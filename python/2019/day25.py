
#!/usr/var/env python3.9

import testfunc as aux
import sys
#from collections import defaultdict

def parse(raw):
    return

def one(data):
    return

def two(data):
    return

if __name__ == "__main__":
    data=aux.timeit(parse, open(sys.argv[1], "r").read(), print_res=False)
    aux.timeit(one, data)
    aux.timeit(two, data)