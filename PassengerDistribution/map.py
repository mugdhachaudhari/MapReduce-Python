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
    value = OvalueList.split(",")
    
    
    try:
        psngr_cnt = int(value[3])
        
    except ValueError:
        continue

    value = 1
    print "%d\t%d" %(psngr_cnt, value)
#     output.write("%d\t%d\n" %( psngr_cnt, value ))
