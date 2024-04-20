# Module UDP.py

# 10 avril 2024

import socket

def UDP_Initialisation():
    global socketptr
    socketptr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        socketptr.connect(('192.168.0.111', 21105))
    except socket.error as e:
        print("Erreur de connexion:", e)

def UDP_Cloture():
    socketptr.close()


def UDP_Send(packet):
    global socketptr
    socketptr.send(packet)


def UDP_Receive():
    global socketptr
    packet, _ = socketptr.recvfrom(100)
    return packet
