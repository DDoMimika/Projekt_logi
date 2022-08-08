import base64
import struct
from read_file import read_file


def decode(pattern_decode, pattern_file):
    encodeline = []
    lines = read_file(pattern_file)
    for line in lines:
        decodedBytes = base64.b64decode(line)
        decodedStr = decodedBytes
        decodedStr = decodedStr
        unpacked = struct.unpack(pattern_decode, decodedStr)
        encodeline.append(list(unpacked))
    return encodeline
