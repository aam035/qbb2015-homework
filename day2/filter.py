#!/usr/bin/env python
filename="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
#check to see if this is correct by typing in terminal ls w ot w/o quotes#

f = open( filename )


#files are itterables that can be used in list, commas surpress new lines after file is printed
for line_count, line in enumerate(f): #enumerate adds the increments and does not need line_count +=1
    if line_count <=10:#limits the lines to 10 to 15
        pass #does nothing
    elif line_count <= 15:
        print line,
    else:
        break #to stop looking through lines
    
    
        
    


