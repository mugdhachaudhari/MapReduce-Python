#!/usr/bin/python

import sys

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
 
current_md = None
current_ttlTrips = 0
days = {'None':0}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
 
     
    md, dt = line.strip().split("\t", 1)
    
#     try:
#         count = int(count)
#         
#     except ValueError:
#         continue

    if md == current_md:
        current_ttlTrips += 1
        if dt not in days:
            days[dt] = 0
    else:
        if current_md:
            vl = [current_ttlTrips, current_ttlTrips/float(len(days))]
            vld =  [current_ttlTrips,"%.2f" % vl[1]]
            vlf = ','.join(map(str, vld))
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%s" %( current_md, vlf )
        current_md = md
        current_ttlTrips = 1
        days = {dt:0}
if current_md:
    vl = [current_ttlTrips, current_ttlTrips/float(len(days))]
    vld =  [current_ttlTrips,"%.2f" % vl[1]]
    vlf = ','.join(map(str, vld))
#     output goes to STDOUT (stream data that the program writes)
    print "%s\t%s" %( current_md, vlf )