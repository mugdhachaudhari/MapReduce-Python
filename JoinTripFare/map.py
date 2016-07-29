#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# inputfileP = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# flp = open(inputfileP,'r')
# output = open(outputfile,'a')

# for line in flp:
    if line.strip() == 'medallion,hack_license,vendor_id,pickup_datetime,payment_type,fare_amount,surcharge,mta_tax,tip_amount,tolls_amount,total_amount':
        continue
    if line.strip() == 'medallion,hack_license,vendor_id,rate_code,store_and_fwd_flag,pickup_datetime,dropoff_datetime,passenger_count,trip_time_in_secs,trip_distance,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude':
        continue
    l = line.strip().split(",")
    if len(l) == 14: #Trip Data
        keylist = [l[0], l[1], l[2], l[5]]
        key = ','.join(keylist)
        valuelist = ['Trip', l[3], l[4], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13]]
        value = ','.join(valuelist)
        print ("%s\t%s" %( key, value ))
#         output.write("%s\t%s\n" %( key, value ))
    else: # Fares Data
#         key = ','.join(l[:4])
        keylist = [l[0], l[1], l[2], l[3]]
        key = ','.join(keylist)
        valuelist = ['Fares', l[4], l[5], l[6], l[7], l[8], l[9], l[10]]
        value = ','.join(valuelist)
	# output goes to STDOUT (stream data that the program writes)
        print ("%s\t%s" %( key, value ))
#         output.write("%s\t%s\n" %( key, value ))

# inputfileS = str(sys.argv[3])
# fls = open(inputfileS,'r')
#  
# for line in fls:
#     if line.strip() == 'medallion,hack_license,vendor_id,pickup_datetime,payment_type,fare_amount,surcharge,mta_tax,tip_amount,tolls_amount,total_amount':
#         continue
#     if line.strip() == 'medallion,hack_license,vendor_id,rate_code,store_and_fwd_flag,pickup_datetime,dropoff_datetime,passenger_count,trip_time_in_secs,trip_distance,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude':
#         continue    
#     l = line.strip().split(",")
#  
#     if len(l) == 14: #Trip Data
#         keylist = [l[0], l[1], l[2], l[5]]
#         key = ','.join(keylist)
#         valuelist = ['Trip', l[3], l[4], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13]]
#         value = ','.join(valuelist)
#         print "%s\t%s" %( key, value )
#         output.write("%s\t%s\n" %( key, value ))
#     else: # Fares Data
#         keylist = [l[0], l[1], l[2], l[3]]
#         key = ','.join(keylist)
#         valuelist = ['Fares', l[4], l[5], l[6], l[7], l[8], l[9], l[10]]
#         value = ','.join(valuelist)
#     # output goes to STDOUT (stream data that the program writes)
#         print "%s\t%s" %( key, value )
#         output.write("%s\t%s\n" %( key, value ))