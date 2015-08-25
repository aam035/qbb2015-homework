#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/rawdata/samples.csv"


df = pd.read_csv(annotation)

print df

for x in df["sample"]:
   df2 = pd.read_table("/Users/cmdb/qbb2015/stringtie/" + x + "/t_data.ctab")
   gene = df2["t_name"].str.contains("FBtr0331261")
   print df2[gene]
    
   

