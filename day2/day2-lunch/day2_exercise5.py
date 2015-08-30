#!/usr/bin/env python

filename="maps_reads.sam"


f = open (filename)

chrm_counter = {'2L':0, '2R':0, '3L':0, '3R':0, '4':0, 'X':0, 'Y':0} #first I need to set a dictionary with keys and values

for lines in f: # then I run a loop to count the number of alignments
    fields = lines.split()# I split the fields to obtain an individual row
    name = fields[2]#specifically where the name is located
    if name in chrm_counter:# this is to say that for every time the name in the files = the name in the dictionary that the alignments should be counted and added to the dict for the values
        chrm_counter[name] += 1
  
print "Here is Chromosome 2L:", chrm_counter["2L"]
print "Here is Chromosome 2R:", chrm_counter["2R"]
print "Here is Chromosome 3L:", chrm_counter["3L"]
print "Here is Chromosome 3R:", chrm_counter["3R"]
print "Here is Chromosome 4:", chrm_counter["4"]
print "Here is Chromosome X:", chrm_counter["X"]
print "Here is Chromosome Y:", chrm_counter["Y"]
     #chrm_counter[align_count]



