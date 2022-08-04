import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import json
from paths import PATH_DATA
import colors

with open(PATH_DATA, "r") as f:
    data = json.load(f)

xpoints = data["PlaneLat"]
ypoints = data["PlaneLon"]
zpoints = data["altitude"]

fig = plt.figure(facecolor=colors.bg_color)

ax = plt.axes(projection="3d")
ax = p3.Axes3D(fig)
lines = ax.plot([], [], [])


def animate(i, lines):
    for line in lines:
        line.set_data(xpoints[: i + 24], ypoints[: i + 24])
        line.set_3d_properties(zpoints[: i + 24])
    return line


anim2 = animation.FuncAnimation(
    fig, animate, frames=int(len(xpoints) / 24), interval=1000, blit=False
)
plt.show()
