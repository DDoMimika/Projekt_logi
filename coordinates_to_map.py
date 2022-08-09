import math


def coordinate_to_pixel(x):
    frac = math.modf(x)[0]
    nx = int(frac * 3600)
    return nx


def pixel_to_coordinate(x, degree):
    nx = x / 3600
    nx += degree


def height_from_coordinates(lat, lon, new_height):
    frac = int(math.modf(lat)[0])
    y = int(frac * len(new_height))
    frac = math.modf(lon)[0]
    x = int(frac * len(new_height))
    return new_height[y][x]
