#!/usr/bin/python

import sys
import StringIO
import csv

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
 
current_key = None
licn = []
tsk1 = []
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:

     
    key, valueList = line.strip().split("\t", 1)
#     print "%s,%s" %(key, valueList ) 
    values = valueList.split(",")
#     print "%s" %(values[0] ) 
    if key == current_key:
#         print "%s" %(values[0] ) 
        if('Licenses' in values[0]):
#             rem = ','.join(values[1:])
            licn.append(values[1:])
        else:
            tsk1.append(values[1:])
#         if('Licenses' in valueList):
#             licn.append(values[1:])
#         else:
#             tsk1.append(values[1:])
    else:
#         print "%s" %(values[0] ) 
        if current_key:
            for tsk in tsk1:
                for lic in licn:
                    print "%s\t%s,%s" %( current_key, ','.join(tsk), ','.join(lic) )
          
        licn = []
        tsk1 = []
        current_key = key
        if('Licenses' in values[0]):
#             print "%s,%s" %(key, valueList ) 
#             csv_file = StringIO.StringIO(values)
#             csv_reader = csv.reader(csv_file)
#             for record in csv_reader:
#                 remvalues = record[1:]
#             rem = ','.join('{0}'.format(w) for w in values[1:])
#             licn.append(rem)
            licn.append(values[1:])
#             print "%s" % (licn)
        else:
            tsk1.append(values[1:])
             
for tsk in tsk1:
    for lic in licn:
        print "%s\t%s,%s" %( current_key, ','.join(tsk), ','.join(lic) )