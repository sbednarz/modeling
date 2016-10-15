# File 15-1.py
# Example 15. Esterification (2)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve

def model(X):
    ch3cooh, etoh, proh, ch3cooet, ch3coopr, water = X
    
    # equilibrium constants
    K1 = 4.9          # ethyl ester
    K2 = 4.2          # propyl ester
    
    # initial concentrations
    c_ch3cooh = 3
    c_proh = 8.0
    c_etoh = 7.0
    
    # model
    eq1 = (ch3cooet * water)/(etoh * ch3cooh) - K1    # equilibrium constant
    eq2 = (ch3coopr * water)/(proh * ch3cooh) - K2    # equilibrium constant
    eq3 = etoh + ch3cooet - c_etoh                     # etoh balance
    eq4 = proh + ch3coopr - c_proh                     # proh balance
    eq5 = ch3cooet + ch3coopr + ch3cooh - c_ch3cooh    # ch3cooh balance
    eq6 = ch3cooet + ch3coopr - water                  # esters bonds balance
    return [eq1, eq2, eq3, eq4, eq5, eq6]
    

# ch3cooh, etoh, proh, ch3cooet, ch3coopr, water
guess = [0.1, 1, 1, 1, 1, 1]  # try different guess values
results = fsolve(model, guess)
ch3cooh, etoh, proh, ch3cooet, ch3coopr, water = results

# report
print "Equilibrium concentrations:"
print "[CH3COOH] = {:.3f} mol/L".format(ch3cooh)
print "[EtOH] = {:.3f} mol/L".format(etoh)
print "[PrOH] = {:.3f} mol/L".format(proh)
print "[CH3COOEt] = {:.3f} mol/L".format(ch3cooet)
print "[CH3COOPr] = {:.3f} mol/L".format(ch3coopr)
print "[H2O] = {:.3f} mol/L".format(water)

