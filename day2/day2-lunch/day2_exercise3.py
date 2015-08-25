#!/usr/bin/env python

filename="maps_reads.sam"

f = open (filename)
file_count = 0

for i in f:
    if "H0:i:1" in i:
        file_count += 1
    
print file_count