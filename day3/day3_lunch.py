#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt


#developing a timecourse
metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")

Sxl = []
Sxl2 = []
for sample in metadata[metadata["sex"] == "female"] ["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")#next filter out particulars
    roi = df["t_name"].str.contains("FBtr0331261")#next grab only values
    Sxl.append(df[roi]["FPKM"].values)

for sample in metadata[metadata["sex"] == "male"] ["sample"]:
    df1 = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")#next filter out particulars
    roi1 = df1["t_name"].str.contains("FBtr0331261")#next grab only values
    Sxl2.append(df1[roi1]["FPKM"].values)

plt.figure()
plt.plot(Sxl, color='r', label = 'female')
plt.plot(Sxl2, color='b', label = 'male')
plt.title("Sxl")
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.legend(['female', 'male'])
xticks = ["10", "11", "12", "13", "14A", "14B", "14C", "14C"]
plt.xticks((range(8)), xticks)
plt.yticks(range(0,301,50))
plt.savefig("timecourse.png")