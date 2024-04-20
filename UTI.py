# UTI.py

import struct
def UTI_TwoBytesLittleEndianToInt(bytes):
    return struct.unpack('<H', bytes)[0]  # Little Endian unsigned short
