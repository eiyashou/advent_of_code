#!/usr/bin/env python

def parse(raw):
    data=tuple(map(int,raw.split("\n")))
    return data

def get_loop_size(num):

    n=1
    l = 0
    while True:

        n = (n*7)%20201227
        l+=1

        if n == num:
            return l


def one(data):
    num1, num2 = data

    n = 1
    for _ in range(get_loop_size(num2)):
        n = (n*num1)%20201227

    return n