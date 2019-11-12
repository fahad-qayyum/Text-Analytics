#!/usr/bin/python
import sys
import re

for line in sys.stdin:
    # getting the 'text' column from the CSV
    array_sentence = line.split(",")[0]
    
    # removing the quotes only if they are at first and last characters
    array_sentence = re.sub(r'^"|"$', '', array_sentence)
    
    # splitting based on space
    text = array_sentence.split()
    for index in range(0, len(text)-1):
        print("%s - %s\t1" % (text[index], text[index + 1].rstrip()))
   

    
       