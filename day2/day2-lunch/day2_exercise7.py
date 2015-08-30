#!/usr/bin/env python

filename="maps_reads.sam"


f = open (filename)

counter=0
total = 0


for lines in f: # then I run a loop to count the number of alignments
    fields = lines.split()# I split the fields to obtain an individual row
    name = fields[2]#specifically where the name is located
    if "@" == lines[0]:
        pass
    else:
        name == "2L" and lines[10000:20000]#from this file I am only looking for the total number of reads for 2L and from those specefic   
    counter += 1
    
print counter