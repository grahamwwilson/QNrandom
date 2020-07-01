from vpython import *
# GlowScript 3.0 VPython
import random
from myrandom import *

# Set up lists with 6 battle-ground states and their electoral-college
# votes. States are ordered from more Democratic to more Republican
# based on 2016 margins
states = ["MI", "WI", "PA", "FL", "NC", "AZ"]
ecvotes = ["16", "10", "20", "29", "15", "11"]
ptilts = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
# list with assumed mean fraction of votes for the Replublican 
# assume no third party candidates, so fraction for the Democrat is 1-f_R
means = [0.475, 0.485, 0.495, 0.505, 0.515, 0.525]
# should check how polling people define errors
errors = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03]

# Assume same result as 2016 for all other states, including
# Maine and Nebraska that use the congressional district method
dbase = 232
rbase = 205

SEED = 206
# initialize the random number generator
random.seed(SEED)

rvictories = 0
dvictories = 0
ties = 0

NINSTANCES = 100000
NTOPRINT = 10

for i in range(NINSTANCES):
    dtot = dbase
    rtot = rbase
    results = []
    for x in range(len(states)):
# roll the dice for what fraction of votes the Republican gets
# based on a normal distribution with an assumed mean and error
        value = NormalVariate(means[x], errors[x])
        if value > 0.50:
            rtot += int(ecvotes[x])
            results.append("R ")
        else:
            dtot += int(ecvotes[x])
            results.append("D ")
    if i < NTOPRINT:
        print('Trial ',i)
        print(states)
        print(results)
        print(ecvotes)
        print('Electoral college total for Republican: ', rtot)
        print('Electoral college total for Democrat:   ', dtot)
        if rtot > dtot:
            print('RED TEAM VICTORY')
        elif dtot > rtot:
            print('BLUE TEAM VICTORY')
        else:
            print('TIE: 269-269')
        print(' ')
    if rtot > dtot:
        rvictories +=1
    elif dtot > rtot:
        dvictories +=1
    else:
        ties +=1

#Summary
print(' ')
print('Summary based on',NINSTANCES,'instances using SEED',SEED)
print('RED TEAM VICTORIES :    ',rvictories)
print('BLUE TEAM VICTORIES:    ',dvictories)
print('ELECTORAL COLLEGE TIES:  ',ties)
    
