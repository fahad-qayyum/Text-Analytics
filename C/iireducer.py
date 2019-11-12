#!/usr/bin/python
import sys;

previous = None
bussL = []

for line in sys.stdin:
    key, value = line.split('\t')
    if key != previous:
        if previous is not None:
            businesses = ""
            for i in range(len(bussL)):
                if i != 0:
                    businesses += ", "
                businesses += bussL[i]
            print(previous + ":" + '\t' + businesses)

            
        previous = key
        bussL = []
    
    buss_num = value.strip()
    if buss_num not in bussL:
        bussL.append(buss_num)
businesses = ""
for i in range(len(bussL)):
    if i != 0:
        businesses += ", "
    businesses += bussL[i]
print(previous + ":" + '\t' + businesses)
     
	
