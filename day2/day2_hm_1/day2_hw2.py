#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt


df1 = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = df1["FPKM"]
top = df2[0:11572]
middle = df2[11572:22144]
end = df2[22144:34718]

plt.figure()
plt.title("fpkm")
plt.boxplot([top, middle, end])
plt.xlabel("location")
plt.ylabel("start position")
plt.savefig("fpkm.png")


  
