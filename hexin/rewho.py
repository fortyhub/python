#!/bin/usr/python

import re
import os


with os.popen('who','r') as f:
    for eachLine in f:
        print(re.split(r'\s\s+|\t',eachLine.rstrip()))

