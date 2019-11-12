#!/usr/bin/python
import sys
import csv
import re

infile = sys.stdin
next(infile)    
for line in infile:
    # getting the 'business_id' column from the CSV
    business_id = line.split(",")[0].strip()
    
    weekday = line.split(",")[1].strip()

    checkins = line.split(",")[3].strip()

    print("%s %s\t%s" % (business_id,weekday,checkins))
        
 
    
   

    
              