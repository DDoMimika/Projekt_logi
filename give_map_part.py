from PIL import Image
from paths import PATH_MAP
from coordinates_to_map import coordinate_to_pixel


def map(minx, maxx, miny, maxy):
    minx = coordinate_to_pixel(minx)
    miny = coordinate_to_pixel(miny)
    maxx = coordinate_to_pixel(maxx)
    maxy = coordinate_to_pixel(maxy)
    if maxx - minx < maxy - miny:
        maxx += (maxy - miny) - (maxx - minx)
    elif maxx - minx > maxy - miny:
        maxy += (maxx - minx) - (maxy - miny)
    im = Image.open(PATH_MAP)
    height = list(im.getdata())
    new_height = []
    for i in range(0, 12960000, 3600):
        new_height.append(height[i : i + 3600])

    new_tab = new_height[miny:maxy]
    final_tab = []
    for x in new_tab:
        new_line = x[minx:maxx]
        final_tab.append(new_line)
    return final_tab
