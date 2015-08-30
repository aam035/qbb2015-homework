#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

blast_file = open ("subset_data_refMrna_data_blastn.txt")


for line in blast_file:
    if line.startswith( ">" ):
        print line.strip(), 
    if "Gaps" and "Identities" in line:
        fields = line.split() 
        gaps = fields[6]
        identities = fields[2]
        print gaps, identities

blast_file.seek(0)
list_scores = []

for line in blast_file: 
    if  " Score = " in line:
        fields = line.split()
        score = float(fields[2])
        list_scores.append(score)
        
plt.figure()
plt.title("Histogram of Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency of Scores")
plt.hist(list_scores, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
plt.savefig("scorehistogram.png")

blast_file.seek(0)
list_evalue = []
for line in blast_file:     
    if  " Expect = " in line:
        fields = line.split()
        evalue = float(fields[7])
        list_evalue.append(evalue)
              
plt.figure()
plt.title("Histogram of Evalues")
plt.xlabel("Evalues")
plt.ylabel("Frequency of Evalues")
plt.hist(list_evalue)
plt.savefig("evaluehistogram.png")

blast_file.seek(0)
plt.figure()
plt.plot(list_scores, list_evalue, 'o')
plt.savefig("ScatterplotofScorevsEvalue.png")
