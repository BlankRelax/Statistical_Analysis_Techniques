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
xData = (rData)**(1/3)
plt.hist(xData,bins=nBins)
plt.show()