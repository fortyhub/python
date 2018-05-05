#!/usr/bin/env python

def f(a):
    sum = 1
    for i in range(a,0,-1):
        sum = sum*i
    return sum
f(7)
