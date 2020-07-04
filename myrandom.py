# myrandom.py
import random
import math

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
