## QNrandom 

python code on modeling using stochastic methods for KU QuarkNet workshop 2020

### Modification notes

Update Jul-8-2020
Code depending on myrandom.py marked with (). These should work as 
designed from command line and Jupyter if running from folder containing
myrandom.py. I don't yet know how to get this to work with Colab. 
For Colab users, you should use the versions with -NoMyRandom in the 
file name when working with the () applications where the myrandom.py 
code is copied directly into the .py file.
example: Gaussian-NoMyRandom.py instead of Gaussian.py

### Code examples in increasing complexity

0  **Uniform.py**
   Starter example with uniform random numbers.

1  **Circle.py**
   Dart-board example for area of unit circle using uniform random numbers

1b **UniformPlot.py**
   Uniform.py but with a histogram

2a (**Gaussian.py**)
   Throw Gaussian random numbers and keep track of statistics for the 
   generated sample. Use the standard normal distribution with mean 
   of zero and variance of 1. For generator implementation 
   details/understanding see later more explicit examples (2d,2e).

2b (**GaussianExplore.py**)
   Essentially the same as 2a, but easier to explore further 
   what is going on, especially in the notebook context

2c (**GaussianPlot.py**)
   Same as Gaussian.py, but also histogram the results, and 
   normalize, and superimpose the expected probability density function.
   Example also keeps track of what fraction of the random numbers 
   are within 1 standard deviation, and how many are outside 1.96 standard 
   deviations.

2d **GaussianGen.py**
   Simple - but expose the details of getting a Gaussian random number 
   from uniform random numbers

2e **GaussianGenPlot.py**
   GaussianGen.py example with plots

3a **ExponentialPlot.py**
   Throw exponential random numbers for the decay time of muons

3b **RadioCarbonDating.py**
   Simulate radioactive decay in the context of dating 
   archaelogical/palaeontological samples using C-14.

4  (**ECGaussianPlot.py**)
   Same as 2c above, but using an assumed mean of 51.5% and 
   a standard deviation of 2.2%. This corresponds to what polling firms 
   would call a 4.3% Margin-of-Error (1.96*2.2% = 4.3%).
   This example allows one to answer the following question. 
   Statistically, if the election in a particular state is correctly 
   characterized by a Gaussian distribution with mean of 51.5% and 
   standard deviation of 2.2%, how often would the candidate who is 
   favored by the poll actually get more than half the cast votes?
   (assumes only two candidates on the ballot).

5a (**ElectoralCollege.py**)
   Simulator for electoral college results based on throwing Gaussian 
   random numbers like in ECGaussianPlot.py for 6 battle-ground states 
   with different numbers of electoral votes.

5b (**ElectoralCollegePlots.py**)
   Add plots and more diagnostics

   **myrandom.py**
   Module with Gaussian random number utilities used in the applications 
   marked with a *.
