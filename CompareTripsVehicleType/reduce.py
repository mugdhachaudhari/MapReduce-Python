#!/usr/bin/python

import sys

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
  
current_vtype = None
current_revenue = 0.00
current_tip = 0.00
current_count = 0
current_tiprevenue = 0.00
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
 
     
    vtype, values = line.strip().split("\t", 1)
    valueList = values.split(",")

    try:
        revenue = float(valueList[0])
        tips = float(valueList[1])
        tiprevenue = float(valueList[2])
        count = int(valueList[3])
    except ValueError:
        continue
    
    if vtype == current_vtype:
        current_revenue += revenue
        current_tip += tips
        current_tiprevenue += tiprevenue
        current_count += count
    else:
        if current_vtype:
            # output goes to STDOUT (stream data that the program writes)
            avgtip = ((current_tiprevenue/current_count)*100)
            
            avgtipa = float(avgtip)
            avgtipb = int(avgtip)
            if avgtipa == avgtipb:
                avgtipp =  str("%.2f" % avgtipb)
            else:
                avgtipa = "%.2f" % (avgtipa)
                avgtipp = str(avgtipa)
                    
            revenuea = float(current_revenue)
            revenueb = int(current_revenue)
            if revenuea == revenueb:
                revenuep = "%.2f" % (revenueb)
            else:
                revenuep = "%.2f" % (revenuea)


        
            print "%s\t%s,%s,%s" %( current_vtype,current_count, revenuep, avgtipp )
        current_vtype = vtype
        current_revenue = float(revenue)
        current_tip = float(tips)
        current_tiprevenue = tiprevenue
        current_count = count
        
if current_vtype:
            # output goes to STDOUT (stream data that the program writes)
    avgtip = float((current_tiprevenue/current_count)*100)
            
    avgtipa = float(avgtip)
    avgtipb = int(avgtip)
    if avgtipa == avgtipb:
        avgtipp =  str("%.2f" % avgtipb)
    else:
        avgtipa = "%.2f" % (avgtipa)
        avgtipp = str(avgtipa)
                    
    revenuea = float(current_revenue)
    revenueb = int(current_revenue)
    if revenuea == revenueb:
        revenuep = "%.2f" % (revenueb)
    else:
        revenuep = "%.2f" % (revenuea)
        
    print "%s\t%s,%s,%s" %( current_vtype,current_count, revenuep, avgtipp )