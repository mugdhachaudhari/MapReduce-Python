#!/usr/bin/python

import sys

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])

# fl = open(inputfile,'r')
 
current_key = None
trips = []
fares = []
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
 
     
    key, valueList = line.strip().split("\t", 1)
    values = valueList.split(',')
    if key == current_key:
        if(values[0] == 'Trip'):
            trips.append(values[1:])
        else:
            fares.append(values[1:])
    else:
        if current_key:
            for trip in trips:
                for fare in fares:
                    print ("%s\t%s,%s" %( current_key, ','.join(trip), ','.join(fare) ))
         
        trips = []
        fares = []
        current_key = key
        if(values[0] == 'Trip'):
            trips.append(values[1:])
        else:
            fares.append(values[1:])
            
for trip in trips:
    for fare in fares:
        print ("%s\t%s,%s" %( current_key, ','.join(trip), ','.join(fare) ))