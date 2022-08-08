import matplotlib.pyplot as plt
import numpy as np

from matplotlib import style
from return_data import return_dataset

data = return_dataset()

p_per_min = 5
gap = p_per_min * (data["time1"][1] - data["time1"][0])

height1 = data["rssi1"]
height2 = data["rssi2"]
x1 = data["time1"]
x2 = data["time2"]

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(111, projection="3d")

if x1[0] > x2[0]:
    tep = [j for j in np.arange(x2[0], x1[0], (gap / 5))]
    nx1 = tep + x1
    nheight1 = ([0] * len(tep)) + height1

for i in range(len(x1) - 1):
    if abs((x1[i]) - (x1[i + 1])) > gap:
        temp = [j for j in np.arange(x1[i], x1[i + 1], (gap / p_per_min))]
        nx1 = nx1[:i] + temp + nx1[i + 1 :]
        nheight1 = nheight1[:i] + ([0] * len(temp)) + nheight1[i + 1 :]

rx2 = []
rheight2 = []

for i in range(len(x2)):
    if x2[i] > x2[0]:
        rx2.append(x2[i])
        rheight2.append(height2[i])
nx2 = rx2
nheight2 = rheight2

for i in range(len(rx2) - 1):
    if abs((rx2[i]) - (rx2[i + 1])) > gap:
        temp = [j for j in np.arange(rx2[i], rx2[i + 1], (gap / 12))]
        nx2 = nx2[:i] + temp + nx2[i + 1 :]
        nheight2 = nheight2[:i] + ([0] * len(temp)) + nheight2[i + 1 :]

y1 = np.zeros(len(nheight1))
z1 = np.zeros(len(nheight1))
width1 = np.ones(len(nheight1))
depth1 = np.ones(len(nheight1))

y2 = np.array([2] * len(nheight2))
z2 = np.zeros(len(nheight2))
width2 = np.ones(len(nheight2))
depth2 = np.ones(len(nheight2))

ax1.bar3d(nx1, y1, z1, width1, depth1, nheight1, color="b", shade=True)
ax1.bar3d(nx2, y2, z2, width2, depth2, nheight2, color="r", shade=True)
blue_proxy = plt.Rectangle((0, 0), 1, 1, fc="b")
red_proxy = plt.Rectangle((0, 0), 1, 1, fc="r")
ax1.legend([blue_proxy, red_proxy], ["rssi tracker", "rssi radio"])
ax1.set_xlabel("time")
ax1.set_ylabel("")
ax1.set_zlabel("rssi")

plt.show()
