import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import colors

from read_data_from_file import return_dataset

p_per_min = 24
interval_time = 1000


def closest(lst, K):

    lst = np.asarray(lst)
    idx = (np.abs(lst - K)).argmin()
    return idx


data = return_dataset()

time = data["time"]
xpoints = data["PlaneLat"]
ypoints = data["PlaneLon"]
zpoints = data["altitude"]

gap = 5 * (data["time1"][1] - data["time1"][0])

height1 = data["rssi1"]
height2 = data["rssi2"]
time1 = data["time1"]
time2 = data["time2"]


nheight1 = [0] * len(time)
nheight2 = [0] * len(time)
for x in time:
    ind1 = closest(time1, x)
    nheight1[ind1] = height1[ind1]
    ind2 = closest(time2, x)
    nheight2[ind2] = height2[ind2]


z = [0]
width = [0.0001]
depth = [0.0001]

fig = plt.figure(facecolor=colors.bg_color)

ax = plt.axes(projection="3d")
ax = p3.Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
nxpoints = []
nypoints = []
for i in range(len(xpoints)):
    nxpoints.append(xpoints[i] + 0.0001)
    nypoints.append(ypoints[i] + 0.0001)
lines = ax.plot(xpoints, ypoints, zpoints, color=colors.plot_color)
signal1 = ax.bar3d(
    nxpoints[0],
    nypoints[0],
    z,
    width,
    depth,
    nheight1[0],
    color=colors.rssi1_color,
    shade=True,
)
signal2 = ax.bar3d(
    xpoints[0],
    ypoints[0],
    z,
    width,
    depth,
    nheight2[0],
    color=colors.rssi2_color,
    shade=True,
)


def animate(i):
    global signal1, signal2
    signal1.remove()
    signal2.remove()
    # rysowac slupeki rssi z najblizszym czasem do tego w ktorym znajdujemy sie z samolotem
    for line in lines:
        line.set_data(xpoints[: i + p_per_min], ypoints[: i + p_per_min])
        line.set_3d_properties(zpoints[: i + p_per_min])
    signal1 = ax.bar3d(
        nxpoints[i],
        nypoints[i],
        z,
        width,
        depth,
        nheight1[i],
        color=colors.rssi1_color,
        shade=True,
    )

    signal2 = ax.bar3d(
        xpoints[i],
        ypoints[i],
        z,
        width,
        depth,
        nheight2[i],
        color=colors.rssi2_color,
        shade=True,
    )


ax.set_xlabel("latitude")
ax.set_ylabel("longitude")
ax.set_zlabel("altitude")
blue_proxy = plt.Rectangle((0, 0), 1, 1, fc=colors.rssi1_color)
red_proxy = plt.Rectangle((0, 0), 1, 1, fc=colors.rssi2_color)
ax.legend([blue_proxy, red_proxy], ["rssi tracker", "rssi radio"])
anim2 = animation.FuncAnimation(
    fig, animate, frames=None, interval=interval_time, blit=False
)
plt.show()
