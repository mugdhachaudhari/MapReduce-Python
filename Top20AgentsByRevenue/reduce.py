#!/usr/bin/python

import sys
import operator
import os
# from collections import OrderedDict

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
  
current_agent_nr = None
current_agent_nm = None
current_revenue = 0.00
# topagn = {'None':0}
topagn = {}
agntrel = {'None':'None'}
k = 20

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
 
     
    keys, revenue = line.strip().split("\t", 1)
    keyList = keys.split(",")
    agent_nr = keyList[0]
    agent_nm = keyList[1]
    

    try:
        revenue = float(revenue)
    except ValueError:
        continue
    
    if agent_nr == current_agent_nr:
        current_revenue += revenue
    else:
        if current_agent_nr:
            # output goes to STDOUT (stream data that the program writes)
            topagn[current_agent_nr] = (current_revenue)
            agntrel[current_agent_nr] = current_agent_nm
        current_agent_nr = agent_nr
        current_agent_nm = agent_nm
        current_revenue = revenue
if current_agent_nr:
# output goes to STDOUT (stream data that the program writes)
    topagn[current_agent_nr] = (current_revenue)
    agntrel[current_agent_nr] = current_agent_nm

if len(topagn) < k:
    k = len(topagn)

# 
# sorted_topagn = OrderedDict(sorted(topagn.items(), key=lambda x: x[1]))
# for i in xrange(len(sorted_topagn), k, -1):
for i in range(0,k):
    tpagntnr = max(topagn.iteritems(), key=operator.itemgetter(1))[0]
#     print "%s" %(tpagntnr)
    max_revenue = "%.2f" % (topagn[tpagntnr])
    tpagntnm = agntrel[tpagntnr]
    print "%s\t%s" %(tpagntnm, max_revenue)
    topagn[tpagntnr]=0.00

        
