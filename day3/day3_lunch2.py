#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

df2 = df[df["FPKM"] > 0] #to get rid of zeros out of the file


plt.figure()
plt.hist(df2["FPKM"].values)
plt.savefig("histogram.png")

plt.figure()
plt.hist(np.log(df2["FPKM"].values))
plt.savefig("histogram.png")




