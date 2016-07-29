#!/usr/bin/python

import sys

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
 
current_psncnt = None
current_sum = 0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
 
     
    psncnt, count = line.strip().split("\t", 1)
    try:
        count = int(count)
    except ValueError:
        continue
    
    if psncnt == current_psncnt:
        current_sum += count
    else:
        if current_psncnt:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d" %( current_psncnt, current_sum )
        current_psncnt = psncnt
        current_sum = count
        
if current_psncnt:
# output goes to STDOUT (stream data that the program writes)
    print "%s\t%d" %( current_psncnt, current_sum )