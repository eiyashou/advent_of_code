import sys, os, re, math, hashlib, itertools, functools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np

# For this one exercise, one gotta paste the input right onto
# a raw string, cause otherwise this shit won't work at all!
raw = r''''''

def one(__):
    return sum(len(line)-len(eval(line)) for line in raw.splitlines())
    
def two(__):
    class Decoder:
        def __init__(self):
            self.regexp = re.compile(r'(\\x\d{2}|"|\\)')
            self.subs = functools.partial(self.regexp.sub, r'\\\1')
            self.prepend = '"'
            self.append = '"'

        def repr(self, s):
            return self.prepend + self.subs(s) + self.append

    decoder = Decoder()
    return sum(len(decoder.repr(line)) - len(line) for line in raw.splitlines())