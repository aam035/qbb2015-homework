#!/usr/bin/env python

filename="maps_reads.sam"

f = open(filename)

count = 0

for  line in f: 
    fields = line.split()
    if line <= 10:
        count+=1
        print fields[2]
    else:
        break




 
    