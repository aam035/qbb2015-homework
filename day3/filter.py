#!/usr/bin/env python
filename="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
#check to see if this is correct by typing in terminal ls w ot w/o quotes#

import sys
# open using arguments:
#print sys.argv
#filename = sys.argv[1]

#f = open( filename )
f = sys.stdin
name_counts = {}

#files are itterables that can be used in list, commas surpress new lines after file is printed
for line_count, line in enumerate(f): #enumerate adds the increments and does not need line_count +=1
     fields = line.split()
     gene_name = fields[9]
     if gene_name not in name_counts:
             name_counts[ gene_name ] = 1
     else:
             name_counts[ gene_name ] += 1

for key, value in name_counts.iteritems():# this is to print out names of new key values in dict
    print key, value
     
    
    
        
    


