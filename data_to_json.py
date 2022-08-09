import json
import patterns
from decode import decode
from paths import DATA_FILENAME_PLOT1, DATA_FILENAME_PLOT2


parametr_time = 1000
parametr_altitude = 100
parametr_PlaneLat = 10000000
parametr_PlaneLon = 10000000

list1 = decode(patterns.pattern03, patterns.pattern03_file)
data = {}
data["time"] = []
data["altitude"] = []
data["PlaneLat"] = []
data["PlaneLon"] = []

for l in list1:
    data["time"].append(l[0] / parametr_time)
    data["altitude"].append(l[1] / parametr_altitude)
    data["PlaneLat"].append(l[2] / parametr_PlaneLat)
    data["PlaneLon"].append(l[3] / parametr_PlaneLon)

data = json.dumps(data)
with open(DATA_FILENAME_PLOT1, "w") as f:
    f.write(data)

list2 = decode(patterns.pattern180, patterns.pattern180_file)
list3 = decode(patterns.pattern181, patterns.pattern181_file)
data2 = {}
data2["rssi1"] = []
data2["time1"] = []
data2["rssi2"] = []
data2["time2"] = []
for l in list2:

    data2["rssi1"].append(l[14])
    data2["time1"].append(l[0] / parametr_time)

for l in list3:
    data2["rssi2"].append(l[29])
    data2["time2"].append(l[0] / parametr_time)

data2 = json.dumps(data2)
with open(DATA_FILENAME_PLOT2, "w") as f:
    f.write(data2)
