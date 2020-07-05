# RadioCarbonDating.py
import random
from myrandom import *
import math
import numpy as np
import matplotlib.pyplot as plot
import scipy.stats as ss

# Use random numbers to estimate the age of a sample in years 
# that has 18% of the expected C-14 fraction of a living sample 
# that is fully equilibrated with the atmospheric C-14 reservoir.

# First assume that we start with N0 C-14 atoms. 
# Either N0 = 100, or N0 = 1000, or N0 = 10000, and we want to use a 
# simulation to figure out how old the sample is, by estimating the 
# range of ages in which NMEASURED = 18, 180 or 1800.
# 
# We run a simulation for as long as it takes to reduce the 
# number of C-14 atoms that are undecayed to <18, <180 or <1800.
# The simulation proceeds time-step by time-step (eg year-by-year, decade-by-decade, or century-by-century).
# Note that depending on your time-step and the particular random number SEED, it may 
# well be that there are multiple simulated years where the C-14 atom count is 
# exactly equalt to NMEASURED.
#
# In contrast to the analytic calculation you did on Tuesday 
# morning, we include probabilistic effects that mean that for 
# any one experimental instance, one does not always take the 
# same number of years to decay down to 18% remaining C-14 atoms, 
# and 18% of the C-14 atoms even corresponds to a time-range even for a given instance.
#
# By running several independent simulations with different random numbers, one can assess 
# how much statistical variation there is in the inferred age. Does it matter 
# whether N0=100 or 1000 or 10000? in this respect?
#
# Changeable parameters:
#     N0    Choose 100, 1000, or 10000
#     DT    Good choices may be 1.0, 10.0, 100.0 (shorter is better - but takes longer)
#     SEED  Any positive integer
#
print()
print('RadioCarbonDating.py Simulation')
print()
HALFLIFE = 5730.0    # C-14 half-life in years
TAU = HALFLIFE       # FIXME - you need to correctly convert from half-life to lifetime (TAU)
print('Half-life set to',HALFLIFE,'years - corresponding lifetime is',TAU,'years.','Is this correct?')

N0 = 1000
DT = 10.0  # Time-step in years (should be short compared to lifetime)
# Initialize the random number generator using specified seed
SEED = 205
random.seed(SEED)

NMEASURED = int(N0*18/100)
print('Start with',N0,'undecayed C-14 atoms')
print('Evolve in time until years when there are',NMEASURED,'undecayed C-14 atoms left')
print('Use time step of',DT,'years and random number seed',SEED)

N = N0
year = 0.0

# probability of decay per time-step
pdecay = 1.0 - math.exp(-DT/TAU)    # obtained by calculating integral(0, DT) (p(t;TAU))
                                    # where p(t;TAU) = 1/TAU exp(-t/TAU)
print('Probability of decay of',pdecay,' per C-14 atom per',DT,' years ')
print(' ')
print('Starting the simulation ')
print(' ')
# Evolved forward in time one year at a time.
while N >= NMEASURED:
    nthrows = 0
# For each undecay C-14 atom that started this year throw a random number to 
# test whether the C-14 atom decayed during this year according to the calculated decay probability 
    for i in range(N):
        u = random.uniform(0.0,1.0)
        nthrows += 1
        if u < pdecay:
            N -= 1      # an atom has decayed
    year += DT
    print('After ',year,' years, undecayed C-14 atoms = ',N,' tested ',nthrows,' C-14 atoms')

print('Finally after',year,' years, undecayed C-14 atoms = ',N)
