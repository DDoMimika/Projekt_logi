import numpy as np
import matplotlib.pyplot as plt
import patterns
from decode import decode
from give_map_part import map

new_height = map(18.0, 18.999, 50.0, 50.999)
list = np.array(decode(patterns.pattern94, patterns.pattern94_file))
nlist = []

yy = []
xx = []

for i in range(len(new_height)):
    ntabx = []
    ntaby = []
    for j in range(len(new_height)):
        ntabx.append(j)
        ntaby.append(i)
    xx.append(ntabx)
    yy.append(ntaby)
fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(
    np.array(xx),
    np.array(yy),
    np.array(new_height),
    cmap="Greens_r",
    linewidth=0,
    antialiased=False,
)

plt.show()
