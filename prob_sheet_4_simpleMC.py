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
rMin = 0.
rMax = 1.
N_array = [1, 2, 4, 12]


for N in N_array:
    y_N=[]
    rData = np.zeros(numVal)
    for i in range(1, N + 1):
        rData = rData+ np.random.uniform(rMin, rMax, numVal)
    y = np.sqrt(12/N)*((rData)-(N / 2))

    plt.hist(y, bins=nBins)
    plt.show()
    print("Mean is "+ str(np.mean(y)))
    print(np.std(y))
    print(np.mean(rData))
    print(np.std(rData))




