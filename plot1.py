from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import json
import colors
from paths import PATH_DATA

with open(PATH_DATA, "r") as f:
    data = json.load(f)

gap = 12 * (data["time"][1] - data["time"][0])
xpoints = data["time"]
ypoints = data["altitude"]
length = len(xpoints) - 1

for i in range(length):
    if abs((xpoints[i]) - (xpoints[i + 1])) > gap:
        temp = [j for j in np.arange(xpoints[i], xpoints[i + 1], (gap / 12))]
        nxpoints = xpoints[:i] + temp + xpoints[i + 1 :]
        nypoints = ypoints[:i] + ([0] * len(temp)) + ypoints[i + 1 :]

tab = []
for i in range(0, len(nypoints) - 1):
    if nypoints[i] != 0 and nypoints[i + 1] == 0:
        tab.append(nxpoints[i])
    elif nypoints[i] == 0 and nypoints[i + 1] != 0:
        tab.append(nxpoints[i])


fig = plt.figure(facecolor=colors.bg_color)
plt1 = fig.add_subplot(111)
plt1.set_facecolor(colors.bg_color_plot)
plt1.axvspan(tab[0], tab[1], color=colors.wrong_color)
plt1.axvspan(nxpoints[0], tab[0], color=colors.correct_color)
plt1.axvspan(tab[1], nxpoints[-1], color=colors.correct_color)
plt.xlabel("Time")
plt.ylabel("Altitude")
plt1.plot(nxpoints, nypoints, color=colors.plot_color)
plt.show()
