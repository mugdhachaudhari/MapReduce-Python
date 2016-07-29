#!/usr/bin/python

import sys
import os
import StringIO
import csv

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# inputfileP = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# flp = open(inputfileP,'r')
# output = open(outputfile,'a')

# for line in flp:
    if line.strip() == 'medallion,name,type,current_status,DMV_license_plate,vehicle_VIN_number,vehicle_type,model_year,medallion_type,agent_number,agent_name,agent_telephone_number,agent_website,agent_address,last_updated_date,last_updated_time':
        continue
    try:
        filename = os.environ['mapreduce_map_input_file']
    except KeyError:
        filename = os.environ['map_input_file']
#     filename = inputfileP
#     print "%s" %( filename )
    if 'license' in filename:
#      if 1 != 1:
# Licenses Data How to determine ????????????????????????????????????????????????
        csv_file = StringIO.StringIO(line)
        csv_reader = csv.reader(csv_file)
        # record is a list containing all the attributes
         
        for record in csv_reader:
            key = record[0]
            if ',' in record[1]:
                value1 = ['"{0}"'.format(record[1])]
            else:
                value1 = [record[1]]
            remvalues = record[2:]
#         lcn = line.strip().split(",")
#         key = lcn[0]
        value = ['Licenses']
#         remvalues = lcn[1:]
            
        value = ['Licenses']
# #         remvalues = csv_reader[1:]
        valuelist = value + value1 + (remvalues)
        vlf = ','.join(valuelist)
#         print "%s" %(valuelist)
#         print "%s" %(vlf)



#         cols = line.strip().split(",")
#         for i in range(1,len(cols)):
#             value = value + "," +cols[i]
#         key = cols[0]
#         vlf = value

        print "%s\t%s" %(key, vlf)
#         output.write("%s\t%s\n" %( key, vlf ))
    else: # Task1 Data
        keys, values = line.strip().split("\t", 1)
        meta = ['Task1']
        splitKeys = keys.split(",")
        key = splitKeys[0]
        splitvalues = values.split(",")
        remkeys = splitKeys[1:]
        fvalues = meta + (remkeys)
        avalues = fvalues + (splitvalues)
        value = ','.join(avalues)

#         value= meta + ","+splitKeys[1] +","+splitKeys[2]+","+splitKeys[3]+","+values


    # output goes to STDOUT (stream data that the program writes)
        print "%s\t%s" %( key, value )
#         output.write("%s\t%s\n" %( key, value ))

# inputfileS = str(sys.argv[3])
# fls = open(inputfileS,'r')
#  
# for line in fls:
#     if line.strip() == 'medallion,name,type,current_status,DMV_license_plate,vehicle_VIN_number,vehicle_type,model_year,medallion_type,agent_number,agent_name,agent_telephone_number,agent_website,agent_address,last_updated_date,last_updated_time':
#         continue
# #     try:
# #         filename = os.environ['mapreduce_map_input_file']
# #     except KeyError:
# #         filename = os.environ['map_input_file']
# #     filename = 'licenses.csv'
# #     print "%s" %( filename )
#     if 'license' in filename:
# #      if 1 != 1:
# # Licenses Data How to determine ????????????????????????????????????????????????
#         csv_file = StringIO.StringIO(line)
#         csv_reader = csv.reader(csv_file)
#         # record is a list containing all the attributes
#          
#         for record in csv_reader:
#             key = record[0]
#             value1 = ['"{0}"'.format(record[1])]
#             remvalues = record[2:]
# #         lcn = line.strip().split(",")
# #         key = lcn[0]
#         value = ['Licenses']
# #         remvalues = lcn[1:]
#             
#         value = ['Licenses']
# # #         remvalues = csv_reader[1:]
#         valuelist = value + value1 + (remvalues)
#         vlf = ','.join(valuelist)
# #         print "%s" %(valuelist)
# #         print "%s" %(vlf)
# 
# 
# 
# #         cols = line.strip().split(",")
# #         for i in range(1,len(cols)):
# #             value = value + "," +cols[i]
# #         key = cols[0]
# #         vlf = value
#         print "%s\t%s" %(key, vlf)
#         output.write("%s\t%s\n" %( key, vlf ))
#     else: # Task1 Data
#         keys, values = line.strip().split("\t", 1)
#         meta = ['Task1']
#         splitKeys = keys.split(",")
#         key = splitKeys[0]
#         splitvalues = values.split(",")
#         remkeys = splitKeys[1:]
#         fvalues = meta + (remkeys)
#         avalues = fvalues + (splitvalues)
#         value = ','.join(avalues)
# 
# #         value= meta + ","+splitKeys[1] +","+splitKeys[2]+","+splitKeys[3]+","+values
#         
#         
#     # output goes to STDOUT (stream data that the program writes)
#         print "%s\t%s" %( key, value )
#         output.write("%s\t%s\n" %( key, value ))