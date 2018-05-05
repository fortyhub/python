#!/usr/bin/env python

def odd():
    n=1
    while True:
        yield n
        n+=2

odd_num = odd()
count = 0
for o in odd_num:
    if count >= 5: break
    print(o)
    count += 1

class Iter:
    def __init__(self):
        self.start=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.start +=2
        return self.start
I = Iter()
for count in range(5):
    print(next(I))
