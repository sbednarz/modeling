# File 12-2.py
# Example 12. Recycle - sequential method
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

FM = 100 # kg/h
alpha = 0.6
xm = 0.05

i = 1 # i = iteration
i_max = 15

print "i\tF0\t\tFR"

# streams
while i < i_max:
    if i == 1:
        FR = 0
    F0 = FM + FR            # mixer (monomer)
    F1P = alpha*F0          # reactor (polymer)
    F1M = F0 - F1P          # reactor (monomer)
    FP = F1P + xm*F1P       # output stream (FP = polymer + monomer)
    FR = F1M - FP*xm        # recycle (monomer balance)
    print "{}\t{:.3f}\t\t{:.3f}".format(i,F0, FR)
    i = i + 1               # next iteration
