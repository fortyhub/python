#!/usr/bin/env python

import time

def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('speed %s' %(end - start))
    return inner

@show_time #foo=show_time()
def foo():
    print("foo...")
    time.sleep(1)
foo()
