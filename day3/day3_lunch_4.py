#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = df["FPKM"] > 0 #can't have the [df[df[""]]] here???

mf = pd.read_table("~/qbb2015/stringtie/SRR072894/t_data.ctab")
mf2 = mf["FPKM"] > 0


b1 = mf2 & df2 #this ensures that both files are even after zeros have been removed
#print b1 #check my work


df3 = df[b1]["FPKM"]
mf3 = mf[b1]["FPKM"]

#print mf3 check work again

df4 = np.log(df3)
mf4 = np.log(mf3)

m = df4 - mf4
a = 0.5 * (df4 + mf4)

plt.figure()
plt.scatter(a, m)
plt.title("MA PLOT")
plt.xlabel("average")
plt.ylabel("mean")
plt.savefig("maplot.png")