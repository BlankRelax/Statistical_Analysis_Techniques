import matplotlib
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return (3*(x**(2)))
numVal = 10000
nBins = 100
x_min =0
x_max = 1
f_max = int(f(x_max))

# Generate uniformly distributed numbers
rMin = 0.
rMax = 1.
rData = np.random.uniform(rMin, rMax, numVal)
x = x_min + rData*(x_max-x_min)
f_x_Data = f(x)
uData= np.random.uniform(rMin, rMax, numVal)*f_max
accepted_x = []
for i in range(1,numVal+1):
    if uData[i-1]<f(x)[i-1]:
        accepted_x.append(x[i-1])

xHist, xbin_edges = np.histogram(accepted_x, bins=nBins, range=(x_min, x_max))
binLo, binHi = xbin_edges[:-1], xbin_edges[1:]
xPlot = np.array([binLo, binHi]).T.flatten()
yPlot = np.array([xHist, xHist]).T.flatten()
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((x_min, x_max))
#ax.set_ylim((0., 800))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot, yPlot)
plt.show()



