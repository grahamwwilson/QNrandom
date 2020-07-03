# QNrandom
python code for KU QuarkNet workshop 2020

Examples in increasing complexity

1. Gaussian.py
   throw Gaussian random numbers and keep track of statistics for the 
   generated sample. Use the standard normal distribution with mean 
   of zero and variance of 1.

2. GaussianPlot.py
   Same as Gaussian.py, but also histogram the results, and 
   normalize, and superimpose the expected probability density function.
   Example also keeps track of what fraction of the random numbers 
   are within 1 standard deviation, and how many are outside 1.96 standard 
   deviations.

3. ECGaussianPlot.py
   Same as 2 above, but using an assumed mean of 51.5% and 
   a standard deviation of 2.2%.

4. ElectoralCollege.py
   Simulator for electoral colege results based on throwing Gaussian 
   random numbers like in ECGaussianPlot.py for 6 battle-ground states.
