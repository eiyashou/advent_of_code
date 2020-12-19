import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np
import regex
from functools import lru_cache

def parse_data(raw):
    r,m = raw.split("\n\n")
    rules = dict()
    for line in r.split("\n"):
        if (p:=re.fullmatch(r"(\d+): (.+)", line)):
            i,rule = p.groups()
            rules[i] = rule.replace("\"","").split(" ")
    return rules, m.split("\n")

@lru_cache
def parse_rule(i, rules):
    if isinstance(rules[i], str): reutrn rules[i]
    frame = "({})" if "|" in rules[i] else "{}"
    return frame.format("".join(parse_rule(ptr, rules) for ptr in rules[i]))

def one(raw):
    rules, msgs = parse_data(raw)

    #Just to make sure it is clean, even though due to how this is set up it will always be clear
    parse_rule.cache_clear()
    ptr = re.compile(parse_rule(0, rules))
    return sum(bool(ptr.fullmatch(line)) for line in msgs)

def two(raw):
    rules, msgs = parse_data(raw)
    
    rules[8] =  ["(?P<eight>", "42", "|", "42", "(?&eight))"]
    rules[11] = ["(?P<eleven>", "42", "31", "|", "42", "(?&eleven)", "31", ")"]

    #Just to make sure it is clean, even though due to how this is set up it will always be clear
    parse_rule.cache_clear()
    ptr = regex.compile(parse_rule(0, rules))
    return sum(bool(ptr.fullmatch(line)) for line in msgs)