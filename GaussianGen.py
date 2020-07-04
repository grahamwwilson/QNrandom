# GaussianGen.py
import random

# Illustrate Gaussian random number generator with more "under-the-hood" details

def StandardNormalVariate():
    # Function to generate a random number from a standard normal distribution
    #
    # Algorithm 1:
    # Use sum of 12 uniform random numbers in range [-0.5,0.5] to approximate a
    # standard normal distribution with mean of 0 and standard deviation of 1.
    # One can prove that this will have a mean of zero and a variance of 1.0.
    # It is not exactly the same as the Gaussian distribution 
    # (for example the range is limited to [-6.0,6.0]), but it is a very good approximation.
    LPRINT = True
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
SEED = 204
random.seed(SEED)

# Generate one random number according to standard normal distribution
z1 = StandardNormalVariate()
print('Obtained z1 = ',z1)
print(' ')

# Generate another random number according to standard normal distribution
z2 = StandardNormalVariate()
print('Obtained z2 = ',z2)

