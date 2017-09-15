"""
A freely-propagating, premixed hydrogen flat flame with multicomponent
transport properties.
"""

from __future__ import print_function
from __future__ import absolute_import
import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
def flameSpeed(phi, P, T):
    p = P*ct.one_atm  # pressure [Pa]
    Tin = T  # unburned gas temperature [K]
    reactants = 'H2:' + str(phi*2) + ' O2:1'  # premixed gas composition
    width = 0.08  # m
    loglevel = 0  # amount of diagnostic output (0 to 8)
    
    # IdealGasMix object used to compute mixture properties, set to the state of the
    # upstream fuel-air mixture
    gas = ct.Solution('h2o2.xml')
    gas.TPX = Tin, p, reactants
    
    # Set up flame object
    f = ct.FreeFlame(gas, width=width)
    f.set_refine_criteria(ratio=3, slope=0.06, curve=0.12)
    f.show_solution()
    
    # Solve with mixture-averaged transport model
    f.transport_model = 'Mix'
    f.solve(loglevel=loglevel, auto=True)
    
    return f.u[0]



ts = [0.5, 1, 2, 3, 4]
phis = np.linspace(250, 750, 30)
us = np.zeros([30,5])

i = 0
j = 0
for t in ts:

    for phi in phis:
        print( phi, t)
        us[i,j] = flameSpeed(1,t,phi)
        i+=1
    j+=1
    i = 0

plt.ylabel('V [m/s]')
plt.xlabel('T [K]')
plt.plot(phis,us[:,0], label="p=0.5 bar")
plt.plot(phis,us[:,1], label="p=1.0 bar")
plt.plot(phis,us[:,2], label="p=2.0 bar")
plt.plot(phis,us[:,3], label="p=3.0 bar")
plt.plot(phis,us[:,4], label="p=4.0 bar")

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
