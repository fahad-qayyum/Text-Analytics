#!/usr/bin/python
import sys
import csv
import re


infile = sys.stdin
next(infile)    
for line in infile:
    # getting the 'business_id' column from the CSV
    catlist = line.rsplit(',', 1)[1]
    
    #catlist = line.split(",")[12]           
    catlist = catlist.split(";")
    
    business_id = line.split(",")[0].strip()
    for category in catlist:
        print("%s\t%s" % (category.strip(), business_id))

