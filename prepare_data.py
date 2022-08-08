import json

from decode import decode
from paths import DATA_FILENAME_PLOT1, DATA_FILENAME_PLOT2


pattern03 = "<4i16hi3b2ib2i2h"
pattern180 = "<I4HI2H4IH18BH2h2BbB2H2b"
pattern181 = "<I4HI2H4IH18BH2h2BbB2H2b"
# "<i4hi2h4ih18b3h4b2hb"
pattern03_file = "*T03"
pattern180_file = "*T180"
pattern181_file = "*T181"


parametr_time = 1000
parametr_altitude = 100
parametr_PlaneLat = 10000000
parametr_PlaneLon = 10000000

list1 = decode(pattern03, pattern03_file)
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

list2 = decode(pattern180, pattern180_file)
list3 = decode(pattern181, pattern181_file)
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
