import matplotlib.pyplot as plt
import numpy as np
import colors

from return_data import return_dataset

data = return_dataset()
gap_p = 12
gap = gap_p * (data["time"][1] - data["time"][0])
xpoints = data["time"]
ypoints = data["altitude"]
length = len(xpoints) - 1
tab = []

for i in range(length):
    if abs((xpoints[i]) - (xpoints[i + 1])) > gap:
        temp = [j for j in np.arange(xpoints[i], xpoints[i + 1], (gap / gap_p))]
        nxpoints = xpoints[:i] + temp + xpoints[i + 1 :]
        nypoints = ypoints[:i] + ([0] * len(temp)) + ypoints[i + 1 :]


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

correct_proxy = plt.Rectangle((0, 0), 1, 1, fc=colors.wrong_color)
wrong_proxy = plt.Rectangle((0, 0), 1, 1, fc=colors.correct_color)

plt.legend([wrong_proxy, correct_proxy], ["signal", "signal lost"])
plt.xlabel("Time")
plt.ylabel("Altitude")

plt1.plot(nxpoints, nypoints, color=colors.plot_color)

plt.show()
