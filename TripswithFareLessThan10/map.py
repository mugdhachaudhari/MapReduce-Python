#!/usr/bin/python

import sys


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
        totalAmt = float(value[16])
    except ValueError:
        continue
#     key = 1
#     value = 1
    key = 1
    count = 1
    if totalAmt <= 10.00:
        print "%s\t%d" %(key, count)

# output.write("%s\t%s\n" %( count, count ))
