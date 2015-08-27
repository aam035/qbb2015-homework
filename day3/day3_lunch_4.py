#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#MA Plots are used to analyze gene expression from microarray data
    #if not logged, the data looks very linear; log allows the user to observe data points that aren't on the linear path
    #by using an MA Plot, we turn the data at a 45 degree angle and compare the average intensity of gene expression to the     mean of gene expression
 
# we need two files to compare and set to zero
df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = df["FPKM"] > 0 #can't have the [df[df[""]]] here???

mf = pd.read_table("~/qbb2015/stringtie/SRR072894/t_data.ctab")
mf2 = mf["FPKM"] > 0


b1 = mf2 & df2 #this ensures that both files are even after zeros have been removed
#print b1 #check my work


df3 = df[b1]["FPKM"]
mf3 = mf[b1]["FPKM"]

#print mf3 check work again

df4 = np.log2(df3) #this takes the log base 2 of the data
mf4 = np.log2(mf3)

m = df4 - mf4 #mean of intensity
a = 0.5 * (df4 + mf4) #average intensity

plt.figure()
plt.scatter(a, m)
plt.title("MA PLOT")
plt.xlabel("average")
plt.ylabel("mean")
plt.savefig("maplot.png")