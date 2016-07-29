#!/usr/bin/python

import sys
import math

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# inputfileP = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# flp = open(inputfileP,'r')
# output = open(outputfile,'a')

# for line in flp:
    Okey, OvalueList = line.strip().split("\t", 1)
    value = OvalueList.split(",")
#     if value[11] <= 0:
#         print "%s" % (line)
    
    try:
        amt = value[11]
#         if amt <= 0:
#             print "%s" % (line)
#         a = float(value[11])
#         b = int(value[11])
#         if a == b:
#             fareAmt = b
#         else:
#             fareAmt = a

#         if fareAmt <= 0:
        fareAmt = float(amt)
#         if fareAmt <= 0:
#             print "%s" % (line)
#             break   
    except ValueError:
        continue
    
#     if fareAmt <= 0:
#         print "%s" % (fareAmt)
    if fareAmt >= 0:
        fareRng = math.ceil(fareAmt / 4)
        if fareAmt == 0:
            valueList = [0, 4]
            fareRng = 1
        elif fareRng == 1:
            valueList = [int(fareRng) - 1, int((fareRng - 1) + 4)]
        elif fareRng >= 13:
#             valueList = [(13 - 1)*4 + 0.01, "float("inf")"]
            fareRng = 13
            valueList = [(13 - 1)*4 + 0.01, "infinite"]
        else:
            valueList = [(fareRng - 1)*4 + 0.01, int(((fareRng - 1)*4) + 4)]
        value = ','.join(map(str, valueList))
            
        print "%02d\t%s" %(fareRng, value)
#         output.write("%s\t%s\n" %( fareRng, value ))
