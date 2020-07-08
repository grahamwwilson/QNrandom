# ECGaussianPlot-NoMyRandom.py
import random
import math
#from myrandom import *    Copied directly in from myrandom.py 
import numpy as np
import matplotlib.pyplot as plot
import scipy.stats as ss

def NormalVariate(mean, rms):
    # Function to generate a random number from a normal distribution with specified
    # mean and rms (aka standard deviation, uncertainty, error, sigma, sqrt(variance))

    # specify algorithm. Algorithm 2 is preferred (algorithm 1 has pedagogical value)
    ALGORITHM = 2

# first generate a random number according to standard normal distribution
# with mean of zero and variance of 1
    if ALGORITHM == 1:
        zValue = StandardNormalVariate1()
    else:
        zValue = StandardNormalVariate2()

# use this zValue to choose random number from the normal distribution with
# specified mean and rms
    normalVariate = mean + rms*zValue
    return normalVariate


def StandardNormalVariate1():
    # Function to generate a random number from a standard normal distribution
    #
    # Algorithm 1:
    # Use sum of 12 uniform random numbers in range [-0.5,0.5] to approximate a
    # standard normal distribution with mean of 0 and standard deviation of 1.
    # One can prove that this will have a mean of zero and a variance of 1.0
    LPRINT = False
    sum = 0.0
    for x in range(12):
        value = random.uniform(-0.5, 0.5)
        sum += value
    zValue = sum
    if LPRINT:
        print("Algorithm 1 zValue ", zValue)
    return zValue


def StandardNormalVariate2():
    # Function to generate a random number from a standard normal distribution
    #
    # Algorithm 2:
    # Use basic form of Box-Muller method to generate standard normal variates
    # (this is NOT an approximation)
    # See https://en.wikipedia.org/wiki/Box-Muller_transform for details
    LPRINT = False
    u1 = random.uniform(0.0, 1.0)
    u2 = random.uniform(0.0, 1.0)
    R = math.sqrt(-2.0*math.log(u1))
# Method yields two independent standard normal variates (z1, z2)
# A more efficient implementation that uses both is easily feasible
# Here we just use the first one, z1.
    z1 = R*math.cos(2.0*math.pi*u2)
    z2 = R*math.sin(2.0*math.pi*u2)
    if LPRINT:
        print("Algorithm 2 chosen zValue ", z1)
    return z1

# --------------------------- START OF MAIN PROGRAM --------------------

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
samplesd = math.sqrt(samplevariance)

# Summary
print(' ')
print('Summary based on',NINSTANCES,'instances using SEED',SEED)
print('Observed mean ',samplemeanx)
print('Observed rms ',samplesd)
print('RESULT <x> = ',samplemeanx,' +- ',samplesd/math.sqrt(NINSTANCES))
print(' ncentral (< 1.0  s.d.) = ',ncentral,' ',100.0*ncentral/NINSTANCES,'%')
print(' noutlier (> 1.96 s.d.) =  ',noutlier,'  ',100.0*noutlier/NINSTANCES,'%')
print(' nrepublican =            ',nrepublican,' ',100.0*nrepublican/NINSTANCES,'%')

# Plot the generated data
plot.hist(xlist, bins=50)
plot.title('Histogram')
plot.xlabel('x = fraction of vote for R')
plot.ylabel('Instances per bin')
plot.show()

rv = ss.norm(0.515,0.022)  # functional form of normal distribution
# Plot it again but this time normalize to an integral of 1
# so that it can be interpreted as a probability density per bin
plot.hist(xlist, density=True, bins=50, label="Data")
plot.title('Normalized Histogram')
plot.xlabel('x = fraction of vote for R')
plot.ylabel('Probability density, p(x)')
x = np.linspace(0.40,0.60)
h = plot.plot(x, rv.pdf(x), lw=2, label="PDF")
plot.legend(loc="upper right")
plot.show()

