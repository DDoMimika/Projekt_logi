import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import colors

from read_data_from_file import return_dataset
from coordinates_to_map import height_from_coordinates
from give_map_part import map
from coordinates_to_map import pixel_to_coordinate

p_per_min = 24
interval_time = 10
data = return_dataset()


def closest(lst, K):

    lst = np.asarray(lst)
    idx = (np.abs(lst - K)).argmin()
    return idx


time = data["time"]
xpoints = data["PlaneLat"]
ypoints = data["PlaneLon"]
zpoints = data["altitude"]

new_height = map(min(xpoints), max(xpoints), min(ypoints), max(ypoints))

nzpoints = []
for i in range(len(zpoints)):
    nzpoints.append(
        zpoints[i] + height_from_coordinates(xpoints[i], ypoints[i], new_height)
    )


gap = 5 * (data["time1"][1] - data["time1"][0])

height1 = data["rssi1"]
height2 = data["rssi2"]
time1 = data["time1"]
time2 = data["time2"]

z = []
nheight1 = [0] * len(time)
nheight2 = [0] * len(time)
for x in time:
    ind1 = closest(time1, x)
    nheight1[ind1] = height1[ind1]
    ind2 = closest(time2, x)
    nheight2[ind2] = height2[ind2]
    z.append(height_from_coordinates(xpoints[ind1], ypoints[ind1], new_height))


width = [0.0001]
depth = [0.0001]

fig = plt.figure(facecolor=colors.bg_color)

ax = plt.axes(projection="3d")
ax = p3.Axes3D(fig, auto_add_to_figure=False, computed_zorder=False)
fig.add_axes(ax)
nxpoints = []
nypoints = []
for i in range(len(xpoints)):
    nxpoints.append(xpoints[i] + 0.0001)
    nypoints.append(ypoints[i] + 0.0001)

yy = []
xx = []

for i in np.arange(
    min(ypoints), max(ypoints), (max(ypoints) - min(ypoints)) / len(new_height)
):
    ntabx = []
    ntaby = []
    for j in np.arange(
        min(xpoints), max(xpoints), (max(xpoints) - min(xpoints)) / len(new_height)
    ):
        ntabx.append(j)
        ntaby.append(i)
    xx.append(ntabx)
    yy.append(ntaby)

surf = ax.plot_surface(
    np.array(xx),
    np.array(yy),
    np.array(new_height),
    cmap="Greens_r",
    linewidth=0,
    antialiased=False,
    zorder=-1,
)

lines = ax.plot(xpoints, ypoints, nzpoints, color=colors.plot_color)
signal1 = ax.bar3d(
    nxpoints[0],
    nypoints[0],
    z[0],
    width,
    depth,
    nheight1[0],
    color="b",
    shade=True,
)
signal2 = ax.bar3d(
    xpoints[0],
    ypoints[0],
    z[0],
    width,
    depth,
    nheight2[0],
    color="r",
    shade=True,
)


def animate(i):
    global signal1, signal2
    signal1.remove()
    signal2.remove()
    for line in lines:
        line.set_data(xpoints[: i + p_per_min], ypoints[: i + p_per_min])
        line.set_3d_properties(nzpoints[: i + p_per_min])
    signal1 = ax.bar3d(
        nxpoints[i],
        nypoints[i],
        z[i],
        width,
        depth,
        nheight1[i],
        color="b",
        shade=True,
    )

    signal2 = ax.bar3d(
        xpoints[i],
        ypoints[i],
        z[i],
        width,
        depth,
        nheight2[i],
        color="r",
        shade=True,
    )


ax.set_xlabel("latitude")
ax.set_ylabel("longitude")
ax.set_zlabel("altitude")
blue_proxy = plt.Rectangle((0, 0), 1, 1, fc="b")
red_proxy = plt.Rectangle((0, 0), 1, 1, fc="r")
ax.legend([blue_proxy, red_proxy], ["rssi tracker", "rssi plane"])
anim2 = animation.FuncAnimation(
    fig,
    animate,
    frames=None,
    interval=interval_time,
    blit=False,
)
plt.show()
