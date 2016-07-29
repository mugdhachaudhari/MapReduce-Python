#!/usr/bin/python

import sys

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
 
current_dt = None
current_revenue = float(0.00)
current_toll = float(0.00)
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
 
     
    dt, values = line.strip().split("\t", 1)
    value = values.split(",")
    try:
        revenue = float(value[0])
        toll = float(value[1])
        
    except ValueError:
        continue

    if dt == current_dt:
        current_revenue += revenue
        current_toll += toll
    else:
        if current_dt:
            # output goes to STDOUT (stream data that the program writes)
            vl = [current_revenue, current_toll]
            vld =  ["%.2f" % e for e in vl]
            vlf = ','.join(map(str, vld))
            print "%s\t%s" %( current_dt, vlf )
        current_dt = dt
        current_revenue = revenue
        current_toll = toll
if current_dt:
    vl = [current_revenue, current_toll]
    vld =  ["%.2f" % e for e in vl]
    vlf = ','.join(map(str, vld))
    print "%s\t%s" %( current_dt, vlf )