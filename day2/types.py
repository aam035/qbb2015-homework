#!/usr/bin/env python

#Integer
i = 100000

#Floating point/real number
f = 0.333

#Changing floating point to integer
i_as_f = float(i)
f_as_i = int(f)

#String
S = "A string"

#Boolean
truthy = True
falsy = False

#Lists- requires [], only contains same type
l = [1,2,3,4,5]
l.append ( 7 )

#Tuple- are mutable, can't add to tuple-- elements can have different types
t = (1, "foo", 5.0)

#Dictionary- function can send lists
d1 = { "key1": "value1", "key2": "value2" }
d2 = dict( key1="value1", key2="value2") 
d3 = dict( [ ("key1", "value1"), ("key2", "value2") ] ) #list of tuples

#Example of publishing in terminal
for value in (i, f, S, truthy, l, t, d1, d2, d3):
    print value, type( value )