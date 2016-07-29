#!/usr/bin/python

import sys
import math

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# inputfileP = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# flp = open(inputfileP,'r')
# output = open(outputfile,'a')

# for line in flp:
    Okey, OvalueList = line.strip().split("\t", 1)
    key = Okey.split(",")
    
    try:
        
        medallion = key[0]
        dt = key[3][:10]

    except ValueError:
        continue
    
    print "%s\t%s" %(medallion, dt)
#     output.write("%s\t%s\n" %( medallion, dt ))
