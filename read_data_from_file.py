import json

from paths import PATH_DATA_PLOT1, PATH_DATA_PLOT2


def return_dataset():
    with open(PATH_DATA_PLOT1, "r") as f:
        data = json.load(f)

    with open(PATH_DATA_PLOT2, "r") as f:
        data.update(json.load(f))

    return data
