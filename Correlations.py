#  Test Correlation Asymmetries
import random
import ROOT
import math
from myrandom import *
import numpy as np
import matplotlib.pyplot as plot
import scipy.stats as ss

# Use Gaussian random number generator

MEAN0  = 0.0
RMS    = 8.0e-6/np.sqrt(2.0)
MEAN1  = 1.0
MEAN2  = 2.0
MEAN3  = 3.0

SEED = 202
# Initialize the random number generator using specified seed
random.seed(SEED)

NINSTANCES = 100000    # Number of experiments to run
NTOPRINT = 5           # Number of experiments to print

# Initialize ROOT file and histograms
hf = ROOT.TFile("Correlations.root", "recreate")
ht0 = ROOT.TH1D("ht0","Correlation Test; t0 (s); Entries per 2 micro-seconds bin",100,-25.0e-6,25.0e-6)
ht4 = ROOT.TH1D("ht4","Correlation Test; t4 (s); Entries per 2 micro-seconds bin",100,1.0-25.0e-6,1.0+25.0e-6)
ht8 = ROOT.TH1D("ht8","Correlation Test; t8 (s); Entries per 2 micro-seconds bin",100,2.0-25.0e-6,2.0+25.0e-6)
hdt40 = ROOT.TH1D("hdt40","Correlation Test; dt40 (s); Entries per 4 micro-seconds bin",100,1.0-50.0e-6,1.0+50.0e-6)
hdt84 = ROOT.TH1D("hdt84","Correlation Test; dt84 (s); Entries per 4 micro-seconds bin",100,1.0-50.0e-6,1.0+50.0e-6)
hA = ROOT.TH1D("hA","Correlation Test; Asymmetry (%); Entries per 1 ppm bin",80,-4.0e-3,4.0e-3)
hA2 = ROOT.TH1D("hA2","Correlation Test; Asymmetry (%); Entries per 1 ppm bin",80,-4.0e-3,4.0e-3)
hACorr = ROOT.TH2D("hACorr","Correlation Test; A(%); A2(%)", 80,-4.0e-3,4.0e-3, 80,-4.0e-3,4.0e-3)
hCorr = ROOT.TH2D("hCorr","Correlation Test; dt40 (s); dt84(s)",80,1.0-50.0e-6,1.0+50.0e-6,80,1.0-50.0e-6,1.0+50.0e-6)
hCorr04 = ROOT.TH2D("hCorr04","Correlation Test; t0 (s); t4(s)",80,-50.0e-6,+50.0e-6,80,1.0-50.0e-6,1.0+50.0e-6)
hCorr08 = ROOT.TH2D("hCorr08","Correlation Test; t0 (s); t8(s)",80,-50.0e-6,+50.0e-6,80,2.0-50.0e-6,2.0+50.0e-6)
hCorr48 = ROOT.TH2D("hCorr48","Correlation Test; t4 (s); t8(s)",80,1.0-50.0e-6,1.0+50.0e-6,80,2.0-50.0e-6,2.0+50.0e-6)

# Generate Gaussian (aka Normal) random numbers with specified MEAN, RMS
for i in range(NINSTANCES):
    t0 = NormalVariate(MEAN0, RMS)  # this function is in myrandom.py
    t4 = NormalVariate(MEAN1, RMS)  # this function is in myrandom.py
    t8 = NormalVariate(MEAN2, RMS)  # this function is in myrandom.py
    t12 = NormalVariate(MEAN3, RMS)  # this function is in myrandom.py

# t0, t4, t8 generated as (hopefully) independent random variates. Let's check
    dt40 = t4-t0
    dt84 = t8-t4
    dtnext = t12-t8
    A = (dt84-dt40)/(dt84+dt40)
    A2 = (dtnext-dt84)/(dtnext+dt84)
# Fill ROOT histograms
    ht0.Fill(t0)
    ht4.Fill(t4)
    ht8.Fill(t8)
    hdt40.Fill(dt40)
    hdt84.Fill(dt84)
    hA.Fill(100.0*A)
    hA2.Fill(100.0*A2)
    hCorr.Fill(dt40,dt84)
    hACorr.Fill(100.0*A, 100.0*A2)
# Also double-check that (t0,t4), (t0,t8) and (t4,t8) are uncorrelated
    hCorr04.Fill(t0,t4)
    hCorr08.Fill(t0,t8)
    hCorr48.Fill(t4,t8)
# Info for first few events
    if i < NTOPRINT:
        print('Trial',i,'(t0,t4,t8)=',t0,t4,t8,'(dt40,dt84)=',dt40,dt84,'A=',A)

# Save ROOT histograms to the file for later inspection
hf.Write()
hf.Close()
