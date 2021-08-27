import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np
from matplotlib.legend_handler import HandlerLine2D

def fiboN2(n):
    if (n < 0): return [[0], [1]]
    if (n < 3): return [[1], [1]]
    current = 1
    previous = 1
    result = [[], []]
    operationsCount = 0
    for i in range(2, n):
        temp = current
        current += previous
        previous = temp
        operationsCount += 3
        result[0].append(operationsCount)
        result[1].append(operationsCount)
    return result

def innerFiboLog(n, count):
    if(n == 1): return [0, 1, count]
    m = n/2
    temp = innerFiboLog(int(m), count+6)
    previous = temp[0]
    current = temp[1]

    prev = (previous * previous) + (current * current)
    cur = current * ((previous * 2) + current)

    if(n % 2 == 0):
        return [prev, cur, temp[2]]
    else:
        return [cur, prev + cur, temp[2]+1]

def fiboLog(n):
    if(n < 1): return 0
    ret = innerFiboLog(n, 1)
    return [ret[2], ret[1]]

n = 200

logX = []
logY = []
n2 = fiboN2(n)
nX = n2[1]
nY = n2[0]
for i in range(1, n):
    log = fiboLog(i)
    logX.append(i)
    logY.append(log[0])

# Fixing random state for reproducibility
np.random.seed(19680801)

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line1, = ax.plot(nX, nY, label='n')
line2, = ax.plot(logX, logY, label='log')

plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})

# create the events marking the x data points
xevents1 = EventCollection(nX, color='tab:blue', linelength=0.05)
xevents2 = EventCollection(logX, color='tab:orange', linelength=0.05)

# create the events marking the y data points
yevents1 = EventCollection(nY, color='tab:blue', linelength=0.05,
                           orientation='vertical')
yevents2 = EventCollection(logY, color='tab:orange', linelength=0.05,
                           orientation='vertical')

# add the events to the axis
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)

# set the limits
ax.set_xlim([1, n])
ax.set_ylim([1, nY[len(nY) - 1]])

ax.set_title('plotting operations count across n2 and log to solve fibo')
plt.show()