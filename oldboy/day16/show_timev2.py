#!/usr/bin/env python

import time

def show_time(func):
    def inner(*x,**y):
        start = time.time()
        func(*x,**y)
        end = time.time()
        print('speed %s' %(end - start))
    return inner

@show_time  #add=show_time(add)
def add(*a,**b):
    count = 0
    for i in a:
        count+=i
    print(count)
    time.sleep(1)

add(1,2,3,4,5,6,7,8,9,10)
