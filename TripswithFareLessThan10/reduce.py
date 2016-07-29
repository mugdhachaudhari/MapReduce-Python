#!/usr/bin/python

import sys

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
 
sum = 0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
 
     
    key, value = line.strip().split("\t", 1)
    try:
        value = int(value)
    except ValueError:
        continue
    sum += value
            # output goes to STDOUT (stream data that the program writes)
print "%d" %( sum )
