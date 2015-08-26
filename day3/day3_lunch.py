#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt


#developing a timecourse
metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
metadata2 = pd.read_csv("/Users/cmdb/qbb2015/rawdata/replicates.csv")

Sxl = []
Sxl2 = []
Sxl3 = []

for sample in metadata[metadata["sex"] == "female"] ["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")#next filter out particulars
    roi = df["t_name"].str.contains("FBtr0331261")#next grab only values
    Sxl.append(df[roi]["FPKM"].values)

for sample in metadata[metadata["sex"] == "male"] ["sample"]:
    df1 = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")#next filter out particulars
    roi1 = df1["t_name"].str.contains("FBtr0331261")#next grab only values
    Sxl2.append(df1[roi1]["FPKM"].values)

for sample in metadata2 ["sample"]:
    df3 = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")#next filter out particulars
    roi3 = df3["t_name"].str.contains("FBtr0331261")#next grab only values
    Sxl3.append(df1[roi1]["FPKM"].values)


plt.figure()
plt.plot(Sxl, color='r', label = 'female')
plt.plot(Sxl2, color='b', label = 'male')
plt.plot([4, 5, 6, 7, 4, 5, 6, 7], Sxl3, 'o', color='g', label = 'replicates')# the x is the numbers and the y is what i made
plt.title("Sxl")
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.legend(['female', 'male'])
xticks = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
plt.xticks((range(8)), xticks)
plt.yticks(range(0,350,50))
plt.savefig("timecourse.png")
