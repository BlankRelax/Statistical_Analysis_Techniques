import matplotlib.pyplot as plt
import numpy as np

numVal = 10000
nBins = 100

rMin = 0.
rMax = 1.
rData = np.random.uniform(rMin, rMax, numVal)
rHist, rbin_edges = np.histogram(rData, bins=nBins, range=(rMin, rMax))
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

xMin = 0
xMax = 1
xData = (rData)**(1/3)
xHist, xbin_edges = np.histogram(xData, bins=nBins, range=(xMin, xMax))
binLo, binHi = xbin_edges[:-1], xbin_edges[1:]
xPlot = np.array([binLo, binHi]).T.flatten()
yPlot = np.array([xHist, xHist]).T.flatten()
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((xMin, xMax))
#ax.set_ylim((0., 800))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot, yPlot)

plt.show()