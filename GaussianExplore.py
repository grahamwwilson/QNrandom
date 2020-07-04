import random
import math
from myrandom import *

# Illustrate Gaussian random number generator
# (here include xlist for after-the-fact exploration)

MEAN  = 0.0
RMS   = 1.0

SEED = 203
# Initialize the random number generator using specified seed
random.seed(SEED)

NINSTANCES = 200       # Number of experiments to run
NTOPRINT = 5           # Number of experiments to print

# Keep track of statistics too
xsum = 0.0
xxsum = 0.0
xlist = []     # Store all generated values here

# Generate Gaussian (aka Normal) random numbers with specified MEAN, RMS
for i in range(NINSTANCES):
    x = NormalVariate(MEAN, RMS)  # this function is in myrandom.py
    xsum += x
    xxsum += x*x
    xlist.append(x)
    if i < NTOPRINT:
        print('Trial ',i,' x = ',x)

# Calculate post-generation statistics
samplemeanx = xsum/float(NINSTANCES)
samplemeanxx = xxsum/float(NINSTANCES)
besselfactor = float(NINSTANCES)/float(NINSTANCES-1)
samplevariance = besselfactor*(samplemeanxx - samplemeanx*samplemeanx)
samplesd = math.sqrt(samplevariance)

# Summary
print(' ')
print('Summary based on',NINSTANCES,'instances using SEED',SEED)
print('Observed mean ',samplemeanx)
print('Observed rms ',samplesd)
print('RESULT <x> = ',samplemeanx,' +- ',samplesd/math.sqrt(NINSTANCES))

# Re-examine some of the values and also print in a fixed format way with 
# not too many significant figures
for i in range(20):
    print('Trial',f'{i:4d}',':',f'{xlist[i]:8.5f}')

for i in range(110,120):
    print('Trial',f'{i:4d}',':',f'{xlist[i]:8.5f}')




