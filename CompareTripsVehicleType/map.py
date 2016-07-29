#!/usr/bin/python

import sys
import math
import StringIO
import csv


vt = ['WAV', 'HYB', 'CNG', 'LV1', 'DSE', 'NRML']
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# inputfileP = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# flp = open(inputfileP,'r')
# output = open(outputfile,'a')


# for line in flp:
    Okey, OvalueList = line.strip().split("\t", 1)
#     print "%s" %(OvalueList)
#     Ov = OvalueList.split(",")
#     print "%s" %(Ov[20])
    csv_file = StringIO.StringIO(OvalueList)
    csv_reader = csv.reader(csv_file)
        # record is a list containing all the attributes
    fare = 0.00
    sc =0.00
    tips =0.00
    vtype = 'None'
    for record in csv_reader:
        try:
#             print "%s" %(record[20])
#             vtype = record[26]
#             fare = float(record[29])
#             sc = float(record[30])
#             tips = float(record[32])
#             print "%s" % (record)
            vtype = record[25]
            fare = float(record[14])
            sc = float(record[15])
            tips = float(record[17]) 
        except ValueError:
            continue
   
#     if vtype in vt:
    revenue = (fare + sc + tips)
    count = 1
    if revenue != 0:        
        tiprevenue = (tips/revenue)
    else:
        tiprevenue = 0
    value = [ (revenue),  (tips), (tiprevenue), count]
    valueList = ','.join(map(str, value))
    
    print "%s\t%s" %(vtype, valueList)
#     output.write("%s\t%s\n" %(vtype, valueList))
