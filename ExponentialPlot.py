# Add some plotting
import random
from myrandom import *
import math
import numpy as np
import matplotlib.pyplot as plot
import scipy.stats as ss

# Random number generator for an exponential distribution

TAU = 2.20  # muon lifetime in micro-seconds

SEED = 202
# Initialize the random number generator using specified seed
random.seed(SEED)

NINSTANCES = 100000      # Number of experiments to run
NTOPRINT = 5           # Number of experiments to print

# Keep track of statistics too
tsum = 0.0
ttsum = 0.0

tlist = []
# Generate random numbers from an exponential distribution with 
# specified lifetime
for i in range(NINSTANCES):
# First generate a random number, u, in range [0,1]
    u = random.uniform(0.0,1.0)
# then use the transformation method 
# (see p207 of Applied Computational Physics for details)
# applied to the exponential distribution to obtain a random time variable, t, 
# that comes from the desired exponential probability density function 
# namely p(t; TAU) = (1/TAU) exp(-t/TAU)
    t = -TAU*math.log(1.0-u)
    tlist.append(t)
    tsum += t
    ttsum += t*t
    if i < NTOPRINT:
        print('Trial ',i,' t = ',t,' (micro-seconds) ')

# Calculate post-generation statistics
samplemeant = tsum/float(NINSTANCES)
samplemeantt = ttsum/float(NINSTANCES)
samplevariance = samplemeantt - samplemeant*samplemeant
samplesd = math.sqrt(samplevariance)

# Summary
print(' ')
print('Summary based on',NINSTANCES,'instances using SEED',SEED)
print('Observed mean ',samplemeant)
print('Observed rms ',samplesd)
print('RESULT <t> = ',samplemeant,' +- ',samplesd/math.sqrt(NINSTANCES))

# Plot the generated data
plot.hist(tlist, bins=50)
plot.title('Histogram')
plot.xlabel('t (micro-seconds)')
plot.ylabel('Decayed muons per bin')
plot.show()

rv = ss.expon(0.0,TAU)  # functional form of exponential distribution
# Plot it again but this time normalize to an integral of 1
# so that it can be interpreted as a probability density per bin
plot.hist(tlist, density=True, bins=50, label="Data")
plot.title('Normalized Histogram')
plot.xlabel('t (micro-seconds)')
plot.ylabel('Probability density, p(t)')
x = np.linspace(0.0,28.0)
h = plot.plot(x, rv.pdf(x), lw=2, label="PDF")
plot.legend(loc="upper right")
plot.show()

# One could also plot this on a log-scale
# (can do this from the histogram window - but may be better to 
#  do it directly in code)

