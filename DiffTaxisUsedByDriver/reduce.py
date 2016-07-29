#!/usr/bin/python

import sys

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
 
current_lc = None
current_md = {'None':0}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
 
     
    lc, md = line.strip().split("\t", 1)

    if lc == current_lc:
        if md not in current_md:
            current_md[md] = 0
    else:
        if current_lc:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%s" %( current_lc, len(current_md) )
        current_lc = lc
        current_md = {md:0} 
if current_lc:
# output goes to STDOUT (stream data that the program writes)
    print "%s\t%s" %( current_lc, len(current_md) )