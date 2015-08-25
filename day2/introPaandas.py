#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None)

#printing first 10 lines
#print df.head()# shows first 5 lines

#print df.describe() #getting information from column 4 and 5
#print df.info()# identifies types

#pull out specefic rows using []; end number is noninclusive
#\n adds new lines
#print "\nthis is what happens with [1:5]\n"
#print df[1:5]
#print "\nthis is what happens with [0:5]\n"
#print df[0:5]
#print "Want rows through 10-15"
#print df[9:15]
#print 20 to 25
#print df[19:25]

#print df.info()
#naming columns and using a list
df.columns = ["chromosome", "database", "type", "start", "end","score", "strand", "frame", "attributes"]
#print df.info()
#sorting infomation
#print df.sort("type", ascending = False)

#subset columns
#print df["chromosome"]
#make lists using two [[]]
#print df[["chromosome", "start", "end"]]

#subset by row ad column
#print df [9:15]["start"] 
#print df.shape#tells the rows of columns
#df2 = df["start"]
#df2 = df[["start", "end"]]
#print df2.shape
#to get rid of commas and straighten columns
#df2.to_csv("startColumn.txt", sep='\t', index=False)

#find only the row in which column 8 = Sxl for example
#find features in annotation in which the start is less than 10

#print df.shape
roi = df["start"] < 10
#type () idenntifies a type of class; ~binary not operator
#print roi.shape
#print df[roi]
print df[roi].shape

#



