#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = df[df["FPKM"] > 0]

df3 = np.log(df2["FPKM"])

plt.figure()
df3.plot(kind = 'kde')
plt.savefig("density.png")
