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
Count_A = 0 #A = Beaf file
Count_B = 0 #B = CTCF file
Count_C = 0 #C = SuHW  
Count_AB = 0
Count_AC = 0
Count_BC = 0
Count_ABC = 0
data = dict(
    list1 = set(list("DM3_Kc_BEAF.bed")),
    list2 = set(list("DM3_Kc_CTCF.bed")),
    list3 = set(list("DM3_Kc_SuHW.bed"))
)
def union( lists1, lists2, lists3 ):
    rval = {}
    for chrom in lists:
        rval[chrom]= lists1[chrom] | lists2[chrom] | lists3[chrom]
    #return rval
      
    for filename in data: #need to combine these and then replace here ii
        for line in open( filename ):
            fields = line.split()
            #parse fields
            chrom = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            #get slice
            slC = C[lists][start:end]
            slB = B[lists][start:end] 
            slA = A[lists][start:end]
              
            if slA.any() | slB.any():
                Count_AB +=1
            elif slA.any() | slC.any():
                Count_AC +=1
            elif slB.any() | slC.any():
                Count_BC +=1
        #return rval       
print Count_AB, Count_AC, Count_BC
'''
plt.figure()
v = venn3(subsets=( Count_AB, Count_AC, Count_BC), set_labels=("BEAF", "CTCF", "SuHW"))
plt.savefig("VennDiagram_union.png")
''' 

