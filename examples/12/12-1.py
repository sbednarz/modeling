# File 12-1.py
# Example 12. Recycle - sequential method
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

FM = 100 # kg/h
alpha = 0.3

i = 1 # i = iteration
i_max = 35

print "i\tF0\t\tF1\t\tFR"

# monomer streams
while i < i_max:
    if i == 1:
        FR = 0
    F0 = FM + FR        # mixer (monomer)
    F1 = F0 - alpha*F0  # reactor (monomer)
    FR = F1             # separator
    print "{}\t{:.3f}\t\t{:.3f}\t\t{:.3f}".format(i,F0, F1, FR)
    i = i + 1           # next iteration
