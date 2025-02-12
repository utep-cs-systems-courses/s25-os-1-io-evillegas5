#! /usr/bin/env python3

import os
import re
import sys
import subprocess


if len(sys.argv) is not 3:
    print("invalid argument count")
    exit()

textFname = sys.argv[0]
outputFile = sys.argv[1]


#fd = os.open(sys.argv[2], os.O_RDONLY)

master = {}

with open(outputFile, 'r') as outputFile:
    for line in outputFile:
        line = line.strip()
        #splits from multiple word boundary delimiters
        word = re.split(r"[\b\W\b]+", line.lower())
        for x in word:
            if x in master:
                master[x] += 1
            else:
                master[x] = 1

masterKeys = list(master.keys())
masterKeys.sort()
sortedMaster = {i: master[i] for i in masterKeys}

fd = os.open(sys.argv[2], os.O_WRONLY | os.O_CREAT)
for key, value in sortedMaster.items():
    newLine = str(key) + " " + str(value) +"\n"
    os.write(fd, newLine.encode())

os.close(fd)
