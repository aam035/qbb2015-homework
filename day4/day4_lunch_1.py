#!/usr/bin/env python

"""
Count intersection of two BED files
"""
#create an array that are all zeros and have length of all chromosomes, find a
#to obtain the arrays and files to use to determine if they are intersect

from __future__ import division #must go first and makes integers floating
import numpy
import sys
from matplotlib_venn  import venn3, venn3_circles
import matplotlib.pyplot as plt

def array_from_len_file( fname ):
    arrays = {} #make a dict
    for line in open( fname ):
        fields = line.split()
        name = fields[0] #to get the first column of names, name here is a list as indicated by the []
        size = int( fields [1] ) #to obtain the second column foor sizes by turning into an int
        arrays[name] = numpy.zeros( size, dtype = bool ) #store key in arrays , will only store as 0, 1 even though a                                                                  boolean was created and type
    return arrays 

def set_bits_from_file( arrays, fname ):
    for line in open( fname ):
        fields = line.split()
        # Parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        arrays[ chrom ][ start : end ] = 1
             
A = array_from_len_file( "dm3.len" ) # the 1 is referring to the file name on the command line
set_bits_from_file( A, "DM3_Kc_BEAF.bed" ) #created arrays for ind files

B = array_from_len_file( "dm3.len" ) 
set_bits_from_file( B, "DM3_Kc_CTCF.bed" )

C = array_from_len_file( "dm3.len" ) 
set_bits_from_file( C, "DM3_Kc_SuHW.bed" )




##for key, value in arrays.iteritems(): 
##    print key, type ( value ), value.shape, numpy.sum( value ) #key is the chromosomes and the value of the arrays
Count_A = 0
Count_B = 0
Count_C = 0
Count_AB = 0
Count_AC = 0
Count_BC = 0
Count_ABC = 0
for filename in ("DM3_Kc_BEAF.bed", "DM3_Kc_CTCF.bed", "DM3_Kc_SuHW.bed"):
    for line in open( filename ):
        fields = line.split()
        #parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        #get slice
        slC = C[chrom][start:end]
        slB = B[chrom][start:end] 
        slA = A[chrom][start:end]
        #print slB.any()
        if slA.any()==True and slB.any()==True and slC.any()==True:
            Count_ABC+=1
        elif slC.any()==True and slB.any()==False and slA.any()==True:
            Count_AC+=1
        elif slC.any()==False and slB.any()==True and slA.any()==True:
            Count_AB+=1
        elif slB.any()==True and slA.any()==False and slC.any()==False:
            Count_B+=1
        elif slB.any()==True and slC.any()==True and slA.any()==False:
            Count_BC+=1
        elif slC.any()==True and slA.any()==False and slB.any()==False:
            Count_C+=1
        elif slA.any()==True and slB.any()==False and slC.any()==False:
            Count_A+=1
          
print Count_ABC, Count_A, Count_AB, Count_AC, Count_BC, Count_B, Count_C
All = int(Count_ABC / 3)
AB = int(Count_AB / 2)
BC = int(Count_BC / 2)
AC = int(Count_AC / 2)
plt.figure()
v = venn3(subsets=(Count_A, Count_B, AB, Count_C, AC, BC, All), set_labels=("BEAF", "CTCF", "SuHW"))
plt.savefig("VennDiagram.png")
