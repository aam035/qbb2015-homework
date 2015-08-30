#!/usr/bin/env python

filename="maps_reads.sam"
#need to calculate mapq scores which is the mean of the total
#going to need two counters, one for the lines and one for the total
# the hint says that if split lines is used then the counter will need to be converted to an int

f = open (filename)

count = 0
total = 0
total_mapq = 0


for lines in f: # then I run a loop to count the number of alignments
    fields = lines.split()# I split the fields to obtain an individual row
    if "@" == lines[0]:
        pass
    else:
        mapq = fields[4]
        count += 1
        total = int(mapq)
        total_mapq += total
        average = total_mapq / count
print average  