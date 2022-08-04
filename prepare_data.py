import json
from decode import decode
from paths import DATA_FILENAME

parametr_time = 1000
parametr_altitude = 100
parametr_PlaneLat = 10000000
parametr_PlaneLon = 10000000
list = decode()
data = {}
data["time"] = []
data["altitude"] = []
data["PlaneLat"] = []
data["PlaneLon"] = []
for l in list:
    data["time"].append(l[0] / parametr_time)
    data["altitude"].append(l[1] / parametr_altitude)
    data["PlaneLat"].append(l[2] / parametr_PlaneLat)
    data["PlaneLon"].append(l[3] / parametr_PlaneLon)

data = json.dumps(data)
with open(DATA_FILENAME, "w") as f:
    f.write(data)
