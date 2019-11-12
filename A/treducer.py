#!/usr/bin/python
from operator import itemgetter
import sys

current_count = 0
current_word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int (count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print("%s\t%s" % (current_word, current_count))
            #file_object.write(str(current_word + "\t" +  str(current_count) + "\n")) 
        current_count = count
        current_word = word
if current_word == word:  
    print("%s\t%s" % (current_word, current_count))
    #file_object.write(str(current_word + "\t" +  str(current_count) + "\n")) 





