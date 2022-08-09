import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import colors

from read_data_from_file import return_dataset

data = return_dataset()
p_per_min = 24
interval_time = 1000

xpoints = data["PlaneLat"]
ypoints = data["PlaneLon"]
zpoints = data["altitude"]

fig = plt.figure(facecolor=colors.bg_color)

ax = plt.axes(projection="3d")
ax = p3.Axes3D(fig)

lines = ax.plot(xpoints, ypoints, zpoints, color=colors.plot_color)


def animate(i):
    for line in lines:
        line.set_data(xpoints[: i + p_per_min], ypoints[: i + p_per_min])
        line.set_3d_properties(zpoints[: i + p_per_min])
    return line


anim2 = animation.FuncAnimation(
    fig, animate, frames=None, interval=interval_time, blit=False
)

ax.set_xlabel("latitude")
ax.set_ylabel("longitude")
ax.set_zlabel("altitude")

plt.show()
