# Add some plotting
import random
from myrandom import *
import numpy as np
import matplotlib.pyplot as plot
import scipy.stats as ss

# Illustrate Gaussian random number generator

MEAN  = 0.515
RMS   = 0.022

SEED = 203
# Initialize the random number generator using specified seed
random.seed(SEED)

NINSTANCES = 100000      # Number of experiments to run
NTOPRINT = 5           # Number of experiments to print

# Keep track of statistics too
xsum = 0.0
xxsum = 0.0
ncentral = 0
noutlier = 0
nrepublican = 0

xlist = []
# Generate Gaussian (aka Normal) random numbers with specified MEAN, RMS
for i in range(NINSTANCES):
    x = NormalVariate(MEAN, RMS)  # this function is in myrandom.py
    xlist.append(x)
    xsum += x
    xxsum += x*x
    normalized_deviation = (x-MEAN)/RMS
    if abs(normalized_deviation) < 1.0:
       ncentral += 1
    if abs(normalized_deviation) > 1.96:
       noutlier += 1
    if x>0.50:
       nrepublican += 1
    if i < NTOPRINT:
        print('Trial ',i,' x = ',x)

# Calculate post-generation statistics
samplemeanx = xsum/float(NINSTANCES)
samplemeanxx = xxsum/float(NINSTANCES)
besselfactor = float(NINSTANCES)/float(NINSTANCES-1)
samplevariance = besselfactor*(samplemeanxx - samplemeanx*samplemeanx)
samplesd = sqrt(samplevariance)

# Summary
print(' ')
print('Summary based on',NINSTANCES,'instances using SEED',SEED)
print('Observed mean ',samplemeanx)
print('Observed rms ',samplesd)
print('RESULT <x> = ',samplemeanx,' +- ',samplesd/sqrt(NINSTANCES))
print(' ncentral (< 1.0  s.d.) = ',ncentral,' ',100.0*ncentral/NINSTANCES,'%')
print(' noutlier (> 1.96 s.d.) =  ',noutlier,'  ',100.0*noutlier/NINSTANCES,'%')
print(' nrepublican =            ',nrepublican,' ',100.0*nrepublican/NINSTANCES,'%')

# Plot the generated data
plot.hist(xlist, bins=50)
plot.title('Histogram')
plot.xlabel('x')
plot.ylabel('Instances per bin')
plot.show()

rv = ss.norm(0.515,0.022)  # functional form of normal distribution
# Plot it again but this time normalize to an integral of 1
# so that it can be interpreted as a probability density per bin
plot.hist(xlist, density=True, bins=50, label="Data")
plot.title('Normalized Histogram')
plot.xlabel('x')
plot.ylabel('Probability density, p(x)')
x = np.linspace(0.40,0.60)
h = plot.plot(x, rv.pdf(x), lw=2, label="PDF")
plot.legend(loc="upper right")
plot.show()

