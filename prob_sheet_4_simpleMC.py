# cauchMC.py -- simple Monte Carlo program to make histogram of uniformly and Cauchy
# distributed random values and plot
# G. Cowan, RHUL Physics, October 2019
# edited for problem sheet 4

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# generate data and store in numpy array, put into histogram

numVal = 10000
nBins = 100
N_array = [1, 2, 4, 12]
y_N = []
for i in range (1,numVal+1):
    for N in N_array:
        # Generate uniformly distributed numbers
        rMin = 0.
        rMax = 1.

        r_i = []
        for i in range(1, N + 1):
            rData = np.random.uniform(rMin, rMax, numVal)
            r_i.append(rData)
        y = np.sqrt(12 / N)*(np.sum(r_i) - (N / 2))
    y_N.append(y)






"""
  # Using transformation method, generate Cauchy distributed numbers
xMin=-10.
xMax=10.
xData = np.tan(np.pi*(rData - 0.5))
xHist, xbin_edges = np.histogram(xData, bins=nBins, range=(xMin, xMax))

# make plots and save in file
binLo, binHi = rbin_edges[:-1], rbin_edges[1:]
xPlot = np.array([binLo, binHi]).T.flatten()
yPlot = np.array([rHist, rHist]).T.flatten()
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((rMin, rMax))
ax.set_ylim((0., 150))
plt.xlabel(r'$r$', labelpad=0)
plt.plot(xPlot, yPlot)

binLo, binHi = xbin_edges[:-1], xbin_edges[1:]
xPlot = np.array([binLo, binHi]).T.flatten()
yPlot = np.array([xHist, xHist]).T.flatten()
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((xMin, xMax))
ax.set_ylim((0., 800))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot, yPlot)

plt.show()
#plt.savefig("histograms.pdf", format='pdf')
"""


