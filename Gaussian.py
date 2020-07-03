from vpython import *
# GlowScript 3.0 VPython
import random
from myrandom import *

# Illustrate Gaussian random number generator

MEAN  = 0.0
RMS   = 1.0

SEED = 202
# initialize the random number generator using specified seed
random.seed(SEED)

NINSTANCES = 100000    # Number of experiments to run
NTOPRINT = 5           # Number of experiments to print

# keep track of statistics too
xsum = 0.0
xxsum = 0.0

# Generate Gaussian (aka Normal) random numbers with specified MEAN, RMS
for i in range(NINSTANCES):
    value = NormalVariate(MEAN, RMS)  # this function is in myrandom.py
    xsum += value
    xxsum += value*value
    if i < NTOPRINT:
        print('Trial ',i,' value = ',value)

# Calculate post-generation statistics
samplemeanx = xsum/float(NINSTANCES)
samplemeanxx = xxsum/float(NINSTANCES)
besselfactor = float(NINSTANCES)/float(NINSTANCES-1)
samplevariance = besselfactor*(samplemeanxx - samplemeanx*samplemeanx)
samplesd = sqrt(samplevariance)

#Summary
print(' ')
print('Summary based on',NINSTANCES,'instances using SEED',SEED)
print('Observed mean ',samplemeanx)
print('Observed rms ',samplesd)
print('RESULT = ',samplemeanx,' +- ',samplesd/sqrt(NINSTANCES))
