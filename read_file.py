import paths


def read_file(pattern):
    with open(paths.PATH_LOG, "r") as f:
        lines = f.readlines()
    telemetries = []
    for line in lines:
        if line.find(pattern) != -1:
            line = line.strip()
            l = line.split(" ")
            telemetries.append(l[3])
    return telemetries
