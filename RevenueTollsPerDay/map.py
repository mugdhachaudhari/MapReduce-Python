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
    key = Okey.split(",")
    
    try:
        
        dt = key[3][:10]
        
        fareamt = float(value[11])
        scamt = float(value[12])
        tipamt = float(value[14])
        tollamt = float(value[15])
        
#         farea = float(fareamt)
#         fareb = int(fareamt)
#         if farea == fareb:
#             fareamt = fareb
#         else:
#             fareamt = farea
#         
#         sca = float(scamt)
#         scb = int(scamt)
#         if sca == scb:
#             scamt = scb
#         else:
#             scamt = sca
#         
#         tipa = float(tipamt)
#         tipb = int(tipamt)
#         if tipa == tipb:
#             tipamt = tipb
#         else:
#             tipamt = tipa
#         
#         tolla = float(tollamt)
#         tollb = int(tollamt)
#         if tolla == tollb:
#             tollamt = tollb
#         else:
#             tollamt = tolla
#         
    except ValueError:
        continue
    
    revenue = fareamt + scamt + tipamt
    vl = [revenue, tollamt]
    vld =  ["%.2f" % e for e in vl]
    vlf = ','.join(map(str, vld))
    print "%s\t%s" %(dt, vlf)
#     output.write("%s\t%s\n" %( dt, vlf ))
