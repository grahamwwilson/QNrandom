# ElectoralCollegePlots.py
import random
from myrandom import *
import matplotlib.pyplot as plot

# The user can change the following parameters that are capitalized
#
# SEED        (to chose a different set of random numbers)
# NINSTANCES  Number of experiments to run
# NTOPRINT    Number of instances to print
# BIAS        Modify the assumed fractions by a constant percentage. For example 0.02 for +2% to R.
# FERROR      Modify the assumed errors by a constant factor. For example 2.0 = double the error.

# Set up python lists with 6 battle-ground states and their electoral-college votes. 
# States are ordered from more Democratic to more Republican based on 2016 margins.
states = ["MI", "WI", "PA", "FL", "NC", "AZ"]
ecvotes = ["16", "10", "20", "29", "15", "11"]

# list with assumed mean fraction of votes for the Republican 
# assume no third party candidates, so fraction for the Democrat is 1-f_R
means = [0.475, 0.485, 0.495, 0.505, 0.515, 0.525] # Each state in toss-up category but MI more D, AZ more R etc.
#means = [0.45, 0.47, 0.49, 0.51, 0.53, 0.55]      # More partisan tilt amongst toss-up states 
#means = [0.50, 0.50, 0.50, 0.50, 0.50, 0.50]      # Each state is a perfect "toss-up"

# should check how polling people define errors. NYTimes/Siena poll had "MoE" of about 0.043.
# this is a 95% CL so need to divide by 1.96, leading to Gaussian error of 0.022.
errors = [0.022, 0.022, 0.022, 0.022, 0.022, 0.022]
#errors = [0.011, 0.011, 0.011, 0.011, 0.011, 0.011]
#errors = [0.044, 0.044, 0.044, 0.044, 0.044, 0.044]

# Assume same result as 2016 for all other states, including ME and NE that use the congressional district method
dbase = 232
rbase = 205

SEED = 206
# initialize the random number generator using specified seed
random.seed(SEED)

rvictories = 0
dvictories = 0
ties = 0

NINSTANCES = 10         # Number of experiments to run
NTOPRINT = 5            # Number of experiments to print

BIAS  = 0.00     # Add a bias per state
FERROR = 1.0      # Increase/decrease the error assumption by a factor
for x in range(len(states)):
    means[x] += BIAS
    errors[x] *= FERROR

# Run all the experiments keeping track of how many votes for each candidate 
# First let's print the assumptions
print('ELECTORAL COLLEGE SIMULATOR based on 6 battle-ground states with following expected vote fractions')
print(states)
print(means)
print(errors)
print()

rlist=[]

for i in range(NINSTANCES):
    rtot = rbase       # Initialize Republican vote total with other states from 2016
    dtot = dbase       # Initialize Democratic vote total with other states from 2016
    results = []
    for x in range(len(states)):
# roll the dice for each battle-ground state to see what fraction of votes 
# the Republican gets based on a normal (aka Gaussian) distribution with the specified 
# means and errors from above
        value = NormalVariate(means[x], errors[x])  # this function is in myrandom.py
        if value > 0.50:
# if the vote total for R exceeds 50%, the R wins
            rtot += int(ecvotes[x])
            results.append("R ")
        else:
# the vote total for D exceeds 50%, so the D wins this state
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
    rlist.append(rtot)
    if rtot > dtot:
        rvictories +=1
    elif dtot > rtot:
        dvictories +=1
    else:
        ties +=1

# Now we should also go through and keep track of all the different 
# outcomes in terms of electoral vote total for the R
# Create a set with one entry for each observed outcome
rset = set(rlist)
print("Observed outcomes in terms of electoral votes for R")
print(sorted(rset))
for x in sorted(rset):
    if x < 269:
       print('R LOSS ',x,'-',538-x,'  # ',rlist.count(x))
    if x == 269:
       print('  TIE  ',x,'-',538-x,'  # ',rlist.count(x))
    if x > 269:
       print('R WIN  ',x,'-',538-x,'  # ',rlist.count(x))

#Summary
print(' ')
print('Summary based on',NINSTANCES,'instances using SEED',SEED)
print('Number of different electoral vote tallies observed',len(rset))
print('RED TEAM VICTORIES :    ',rvictories,'  ',100.0*rvictories/NINSTANCES,'%')
print('BLUE TEAM VICTORIES:    ',dvictories,'  ',100.0*dvictories/NINSTANCES,'%' )
print('ELECTORAL COLLEGE TIES:  ',ties,'   ',100.0*ties/NINSTANCES,'%')

# Plot the generated data
plot.hist(rlist, bins=120)
plot.title('Electoral College Histogram')
plot.xlabel('Electoral Votes for R')
plot.ylabel('Election Instances per bin')
#plot.show()   

