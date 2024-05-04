# Lecon n°2 de Gabrielle
#
# Creation chatgpt :
#
#  "Notez que j'ai utilisé les modules socket et struct de Python
# pour les opérations de réseau et de manipulation de données binaires."
#
# Ajout de l'interface 06-04-2024
# Modif le 04-05-2024
# Modif Custom-TKinter
# Suppression des modules : UDP.py , UTI.py, LAN.py

import customtkinter
from PIL import Image
import socket
import time
import struct

bg_color = '#048b9a'
fg_color = '#02454d'
app = customtkinter.CTk()
WAIT_PACKET = 0.04  # 40 milliseconds
my_font = ("arial", 24)

# UDP ###############################################
def UDP_Initialisation():
    try:
        socketptr.connect(('192.168.0.111', 21105))
    except socket.error as e:
        print("Erreur de connexion:", e)

def UDP_Cloture():
    socketptr.close()

def UDP_Send(packet):
    socketptr.send(packet)

def UDP_Receive():
    packet, _ = socketptr.recvfrom(100)
    return packet

# LAN #################################################
SERIAL_NUMBER = 0x10  # Request Serial Code

def LAN_GET_SERIAL_NUMBER():
    packet = b'\x04\x00' + bytes([SERIAL_NUMBER]) + b'\x00'
    UDP_Send(packet)

def LAN_GET_SERIAL_NUMBER_RESP():
    header, data = LAN_lecture()
    if header == SERIAL_NUMBER:
        NumeroSerie = struct.unpack('<I', data)[0]  # Little Endian unsigned int
        return NumeroSerie
    return None

def LAN_lecture():
    packet = UDP_Receive()
    if len(packet) < 4:
        print("Packet invalide de moins de 4 Octets")
        return None, None
    datalen = struct.unpack('<H', packet[:2])[0]  # Little Endian unsigned short
    header = struct.unpack('<H', packet[2:4])[0]  # Little Endian unsigned short
    data = packet[4:]
    return header, data

##########################################################

def action():
    NumeroSerie = Z21_LireNumSerie()
    if NumeroSerie is not None:
        vartext = str(NumeroSerie)
        result = customtkinter.CTkLabel(master=app, text=vartext, fg_color="transparent", font=my_font)
        result.grid(row=1, column=1, padx=20, pady=20)
        print(vartext)
        print("Numéro de série est", NumeroSerie)
    else:
        print("Erreur dans la fonction Z21_LireNumSerie()")
    
def Z21_LireNumSerie():
    NumeroSerie = 0
    LAN_GET_SERIAL_NUMBER()
    time.sleep(WAIT_PACKET)  # Attente 40ms pour avoir la réponse.
    return LAN_GET_SERIAL_NUMBER_RESP()

def main():
    app.geometry("450x200")
    app.title("CTk example")
    button = customtkinter.CTkButton(master=app, text="SERIAL", font=my_font, command=action)
    button.grid(padx=20, pady=20, row=1, column=0)
    my_image = customtkinter.CTkImage(light_image=Image.open("z21_small.png"), size=(400, 76))
    image_label = customtkinter.CTkLabel(app, image=my_image, text="")
    image_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
    app.mainloop()
    return 0

if __name__ == "__main__":
    socketptr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_Initialisation()
    main()
    UDP_Cloture()
