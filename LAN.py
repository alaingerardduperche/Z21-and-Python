# LAN.py

import struct
import UDP

SERIAL_NUMBER = 0x10  # Request Serial Code

def LAN_GET_SERIAL_NUMBER():
    packet = b'\x04\x00' + bytes([SERIAL_NUMBER]) + b'\x00'
    UDP.UDP_Send(packet)

def LAN_GET_SERIAL_NUMBER_RESP():
    header, data = LAN_lecture()
    if header == SERIAL_NUMBER:
        NumeroSerie = struct.unpack('<I', data)[0]  # Little Endian unsigned int
        return NumeroSerie
    return None


def LAN_lecture():
    packet = UDP.UDP_Receive()
    if len(packet) < 4:
        print("Packet invalide de moins de 4 Octets")
        return None, None
    datalen = struct.unpack('<H', packet[:2])[0]  # Little Endian unsigned short
    header = struct.unpack('<H', packet[2:4])[0]  # Little Endian unsigned short
    data = packet[4:]
    return header, data
