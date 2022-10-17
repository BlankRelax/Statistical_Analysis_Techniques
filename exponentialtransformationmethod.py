import matplotlib.pyplot as plt
import numpy as np

numVal = 100000
nBins = 100

rMin = 0.
rMax = 1.
rData = np.random.uniform(rMin, rMax, numVal)
plt.hist(rData, bins=nBins, range = (rMin,rMax))
plt.show()

xMin = 0
xMax = 8.5
xData = -np.log(1-rData)
plt.hist(xData,bins=nBins, range=(xMin,xMax))
plt.show()