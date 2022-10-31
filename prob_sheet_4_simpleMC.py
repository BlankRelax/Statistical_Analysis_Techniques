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
    y = 0
    rData = np.zeros(numVal)#reset the array for each calculation of y_N
    for i in range(1, N + 1):
        rData = rData+ np.random.uniform(rMin, rMax, numVal) # calculatng x_N by summing over random variable generated using np.random.uniform
    y = np.sqrt(12/N)*((rData)-(N / 2))

    rHist, rbin_edges = np.histogram(y, bins=nBins, range=(-4, 4))
    # make plots and save in file
    binLo, binHi = rbin_edges[:-1], rbin_edges[1:]
    xPlot = np.array([binLo, binHi]).T.flatten()
    yPlot = np.array([rHist, rHist]).T.flatten()
    fig, ax = plt.subplots(1, 1)
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.gcf().subplots_adjust(left=0.15)
    ax.set_xlim((-4, 4))
    ax.set_ylim((0., 400))
    plt.xlabel(r'$r$', labelpad=0)
    plt.ylabel("y_N")
    plt.plot(xPlot, yPlot, label = "Mean=" +str(round(np.mean(y),4)) +"  SD=" +str(round(np.std(y),4)) + "  Mean of x_N= " + str(round(np.mean(rData),4))+  "  SD of x_N= " + str(round(np.std(rData),4)))
    leg = ax.legend()
    plt.show()














