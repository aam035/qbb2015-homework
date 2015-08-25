#!/usr/bin/env python
filename="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
#check to see if this is correct by typing in terminal ls w ot w/o quotes#

f = open( filename )

#files are itterables that can be used in list, commas surpress new lines after file is printed
for line in f:
    fields = line.split()
    if "tRNA" in fields[9]:
        print line,


