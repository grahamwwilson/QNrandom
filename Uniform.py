# Uniform.py
import random

# Illustrate standard uniform random number generator

# Initialize the random number generator using specified seed
SEED = 203
random.seed(SEED)

NINSTANCES = 10         # Number of random numbers to generate

# Generate uniform random numbers
for i in range(NINSTANCES):
    u = random.random() # standard uniform random numbers 
                        # in range [0.0,1.0)
    print('uniform random number',i,'u =',u)
