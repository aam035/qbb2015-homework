#!/usr/bin/env python

filename="maps_reads.sam"

f = open (filename)
align_count = 0

for lines in f:
    align_count += 1
    
print align_count
    