# UniformPlot.py
import random
import math
import matplotlib.pyplot as plot

# Illustrate standard uniform random number generator

# Initialize the random number generator using specified seed
SEED = 203
random.seed(SEED)

NINSTANCES = 1000         # Number of random numbers to generate

ulist=[]
usum = 0.0
uusum = 0.0

# Generate uniform random numbers
for i in range(NINSTANCES):
    u = random.random() # standard uniform random numbers 
                        # in range [0.0,1.0)
    usum += u
    uusum += u*u
    ulist.append(u)
#    print('uniform random number',i,'u =',u)

# Calculate post-generation statistics
samplemeanu = usum/float(NINSTANCES)
samplemeanuu = uusum/float(NINSTANCES)
besselfactor = float(NINSTANCES)/float(NINSTANCES-1)
samplevariance = besselfactor*(samplemeanuu - samplemeanu*samplemeanu)
samplesd = math.sqrt(samplevariance)

# Summary
print(' ')
print('Summary based on',NINSTANCES,'instances using SEED',SEED)
print('Observed mean ',samplemeanu)
print('Observed rms ',samplesd)
print('RESULT <u> = ',samplemeanu,' +- ',samplesd/math.sqrt(NINSTANCES))

# Plot the generated data
plot.hist(ulist, bins=50)
plot.title('Uniform Distribution Histogram')
plot.xlabel('u')
plot.ylabel('Instances per bin')
plot.show()
