import paths

pattern = "*T03"


def read_file():
    with open(paths.PATH_LOG, "r") as f:
        lines = f.readlines()
    telemetries_03 = []
    for line in lines:
        if line.find(pattern) != -1:
            line = line.strip()
            l = line.split(" ")
            telemetries_03.append(l[3])
    return telemetries_03
