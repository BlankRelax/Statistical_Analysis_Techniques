# cauchMC.py -- simple Monte Carlo program to make histogram of uniformly and Cauchy
# distributed random values and plot
# G. Cowan, RHUL Physics, October 2019

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# generate data and store in numpy array, put into histogram
numVal = 10000
nBins = 100

# Generate uniformly distributed numbers
rMin = 0.
rMax = 1.
rData = np.random.uniform(rMin, rMax, numVal)
print(rData)
rHist, rbin_edges = np.histogram(rData, bins=nBins, range=(rMin, rMax))
plt.hist(rData,bins=nBins, range=(rMin, rMax))
plt.show()
# Using transformation method, generate Cauchy distributed numbers
xMin=-10.
xMax=10.
xData = np.tan(np.pi*(rData - 0.5))
xHist, xbin_edges = np.histogram(xData, bins=nBins, range=(xMin, xMax))
plt.hist(xData,bins=nBins, range=(xMin, xMax))
plt.show()

# make plots and save in file
binLo, binHi = rbin_edges[:-1], rbin_edges[1:]
xPlot = np.array([binLo, binHi]).T.flatten()
yPlot = np.array([rHist, rHist]).T.flatten() # this plots histogram of uniformly random distributed data
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((rMin, rMax))
ax.set_ylim((0., 150))
plt.xlabel(r'$r$', labelpad=0)
plt.plot(xPlot, yPlot)

binLo, binHi = xbin_edges[:-1], xbin_edges[1:]
xPlot = np.array([binLo, binHi]).T.flatten()
yPlot = np.array([xHist, xHist]).T.flatten() # this plot histogram of transformed variable
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((xMin, xMax))
ax.set_ylim((0., 800))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot, yPlot)

plt.show()
plt.savefig("histograms.pdf", format='pdf')

