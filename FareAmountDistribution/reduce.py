#!/usr/bin/python

import sys

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
 
current_range = None
current_sum = 0
current_value = None
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
 
     
    range, value = line.strip().split("\t", 1)
#     try:
#         count = int(count)
#     except ValueError:
#         continue
    
    if range == current_range:
        current_sum += 1
    else:
        if current_range:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d" %( current_value, current_sum )
        current_range = range
        current_value = value
        current_sum = 1
if current_range:
    print "%s\t%d" %( current_value, current_sum )