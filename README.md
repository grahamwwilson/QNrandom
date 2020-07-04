# QNrandom
python code for KU QuarkNet workshop 2020

Examples in increasing complexity

-1 Circle.py
   dart-board example for area of unit circle

0. ExponentialPlot.py
   throw exponential random numbers for the decay time of muons

1a. Gaussian.py
   throw Gaussian random numbers and keep track of statistics for the 
   generated sample. Use the standard normal distribution with mean 
   of zero and variance of 1.

1b. GaussianExplore.py
   Essentially the same as 1a, but easier to explore further 
   what is going on, especially in the notebook context

2. GaussianPlot.py
   Same as Gaussian.py, but also histogram the results, and 
   normalize, and superimpose the expected probability density function.
   Example also keeps track of what fraction of the random numbers 
   are within 1 standard deviation, and how many are outside 1.96 standard 
   deviations.

3. ECGaussianPlot.py
   Same as 2 above, but using an assumed mean of 51.5% and 
   a standard deviation of 2.2%. This corresponds to what polling firms 
   would call a 4.3% Margin-of-Error (1.96*2.2% = 4.3%).
   This example allows one to answer the following question. 
   Statistically, if the election in a particular state is correctly 
   characterized by a Gaussian distribution with mean of 51.5% and 
   standard deviation of 2.2%, how often would the candidate who is 
   favored by the poll actually get more than half the cast votes?
   (assumes only two candidates on the ballot).

4. ElectoralCollege.py
   Simulator for electoral college results based on throwing Gaussian 
   random numbers like in ECGaussianPlot.py for 6 battle-ground states 
   with different numbers of electoral votes.
