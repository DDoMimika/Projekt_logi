import base64
import struct
from read_file import read_file

pattern = "<4i16hi3b2ib2i2h"


def decode():
    encodeline = []
    lines = read_file()
    for line in lines:
        decodedBytes = base64.b64decode(line)
        decodedStr = decodedBytes
        unpacked = struct.unpack(pattern, decodedStr)
        encodeline.append(list(unpacked))
    print(encodeline[0])
    return encodeline
