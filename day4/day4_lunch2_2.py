#!/usr/bin/env python

"""
Count intersection of two BED files
"""

from __future__ import division

import sys

import chrombits


arr = chrombits.ChromosomeLocationBitArrays( fname =sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()

ctcf.set_bits_from_file( sys.argv[2] )

new = ctcf.new()# to read files

print new

#second part of b
#A.sets_bits_from_file(fname= sys.argv[3])
#B.sets_bits_from_file(fname= sys.argv[4])

#A_and_not_B = A.intersect(B.complement())
#tuple_list = A_and_not_B.new()
#print tuple_list