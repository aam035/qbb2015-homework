#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None)

df.columns = ["chromosome", "database", "type", "start", "end","score", "strand", "frame", "attributes"]

gene = df["attributes"].str.contains("Sxl")

plt.figure()
plt.title("Accounts of Sxl")
plt.plot(df[gene]["start"])
plt.xlabel("gene")
plt.ylabel("start position")
plt.savefig("starts.png")