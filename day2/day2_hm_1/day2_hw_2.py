#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None)

df.columns = ["chromosome", "database", "type", "start", "end","score", "strand", "frame", "attributes"]

gene = df["attributes"].str.contains("Sxl")
df2 = df[gene]
d2 = df2["type"].str.contains("transcript")
plt.figure()
plt.title("Sxl and Transcript Positions")
plt.plot(df2[d2]["start"])
plt.xlabel("gene")
plt.ylabel("start position")
plt.savefig("sxl and trans.png")


