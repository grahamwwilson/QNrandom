# GaussianGenPlot.py
import random
import math
import numpy as np
import matplotlib.pyplot as plot
import scipy.stats as ss

# Illustrate Gaussian random number generator
# using standard distribution (mean = 0.0 and standard deviation of 1.0) for starters

def StandardNormalVariate():
    # Function to generate a random number from a standard normal distribution
    #
    # Algorithm 1:
    # Use sum of 12 uniform random numbers in range [-0.5,0.5] to approximate a
    # standard normal distribution with mean of 0 and standard deviation of 1.
    # One can prove that this will have a mean of zero and a variance of 1.0
    LPRINT = False
    usum = 0.0
    for i in range(12):
        u = random.uniform(-0.5, 0.5)
        if LPRINT:
            print('i = ',i,' u = ',u)
        usum += u
    zValue = usum
    if LPRINT:
        print('zValue ', zValue)
    return zValue

# Initialize the random number generator using specified seed
SEED = 302
random.seed(SEED)

NINSTANCES = 100000       # Number of experiments to run
NTOPRINT = 5
NDOF = 100

# Keep track of statistics too
xsum = 0.0
xxsum = 0.0
ncentral = 0
noutlier = 0

#xlist = []
Qlist = []
# Generate standard Gaussian (aka Normal) random numbers
for i in range(NINSTANCES):
    Q = 0.0
    for j in range(NDOF):
        x = StandardNormalVariate()
        Q += x*x
#        xlist.append(x)
        xsum += x
        xxsum += x*x
        if abs(x) < 1.0:
           ncentral += 1
        if abs(x) > 1.96:
           noutlier += 1
        if i < NTOPRINT:
           print('Trial ',i,' x = ',x)
    if i < NTOPRINT:
       print('Trial ',i,' Q = ',Q)
    Qlist.append(Q)

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
print(' ncentral (< 1.0  s.d.) = ',ncentral,' ',100.0*ncentral/NINSTANCES,'%')
print(' noutlier (> 1.96 s.d.) =  ',noutlier,'  ',100.0*noutlier/NINSTANCES,'%')

# Plot the generated data
plot.hist(Qlist, bins=100)
plot.title('Histogram of Chi-Squared Distribution (ndof=100)')
plot.xlabel('x')
plot.ylabel('Instances per bin')
plot.show()

rv = ss.norm(0.0,1.0)  # functional form of standard normal distribution
# Plot it again but this time normalize to an integral of 1
# so that it can be interpreted as a probability density per bin
plot.hist(Qlist, density=True, bins=50, label="Data")
plot.title('Normalized Histogram')
plot.xlabel('Chi-squared')
plot.ylabel('Probability density, p(x)')
x = np.linspace(0.0,200.0)
h = plot.plot(x, rv.pdf(x), lw=2, label="PDF")
plot.legend(loc="upper right")
plot.show()
