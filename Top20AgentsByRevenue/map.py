#!/usr/bin/python

import sys
import math
import StringIO
import csv

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# inputfileP = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# flp = open(inputfileP,'r')
# output = open(outputfile,'a')

# for line in flp:
    Okey, OvalueList = line.strip().split("\t", 1)
    values = OvalueList.split(",")
    try:
        fare = float(values[14])
        sc = float(values[15])
        tips = float(values[17])
        agent_nr = values[28]
        agent_nm = values[29]
#         print "%s" %(values)
    except ValueError:
        continue
    csv_file = StringIO.StringIO(OvalueList)
    csv_reader = csv.reader(csv_file)
        # record is a list containing all the attributes
    fare = 0.00
    sc =0.00
    tips =0.00
    agent_nr = 'None'
    agent_nm = 'None'
    for record in csv_reader:
        try:
#             print "%s" %(record[20])
#             vtype = record[26]
#             fare = float(record[29])
#             sc = float(record[30])
#             tips = float(record[32])
#             print "%s" % (record)
            fare = float(record[14])
            sc = float(record[15])
            tips = float(record[17])
            agent_nr = record[28]
            agent_nm = record[29]
        except ValueError:
            continue

    revenue = fare + sc + tips
    key = [agent_nm]
    key = [agent_nr, agent_nm]
    keyList = ','.join(key)
    value = ["%.2f" % revenue]
    vlf = ','.join(map(str, value))
    print "%s\t%s" %(keyList, vlf)
#     output.write("%s\t%s\n" %(keyList, vlf))
