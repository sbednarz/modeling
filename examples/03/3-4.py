# File 3-4.py
# Example 3. Calculations with Python
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

a = []               # create empty list
b = [0, 21]          # create two-elements list
c = [1.3, 1.3e-3, 3] # create three-element list
print a
print b
print c

e1 = c[0]            # unpack elements; approach 1
e2 = c[1]
e3 = c[2]
print e1
print e2
print e3

ee1, ee2, ee3 = c    # unpack list; approach 2
print ee1, ee2, ee3  # print variables


