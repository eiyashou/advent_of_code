import sys, os, re, math, hashlib, itertools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np
import regex

def parse_data(raw):
    r,m = raw.split("\n\n")
    rules = dict()
    for line in r.split("\n"):
        if (p:=re.fullmatch(r"(\d+): (.+)", line)):
            i,rule = p.groups()
            rules[i] = rule.replace("\"","").split(" ")
    return rules, m.split("\n")


def parse_rule(i, rules):
    rules[i] = rules[i] if isinstance(rules[i], str) else "("+"".join(parse_rule(ptr, rules) for ptr in rules[i])+")"
    return rules[i]

def one(raw):
    rules, msgs = parse_data(raw)

    ptr = re.compile(parse_rule(0, rules))
    return sum(bool(ptr.fullmatch(line)) for line in msgs)

def two(raw):
    rules, msgs = parse_data(raw)
    
    rules[8] =  ["(?P<eight>", "42", "|", "42", "(?&eight))"]
    rules[11] = ["(?P<eleven>", "42", "31", "|", "42", "(?&eleven)", "31", ")"]
    
    ptr = regex.compile(parse_rule(0, rules))
    return sum(bool(ptr.fullmatch(line)) for line in msgs)