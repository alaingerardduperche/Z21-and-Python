# Lecon n°2 de Gabrielle
#
# Creation chatgpt :
#
#  "Notez que j'ai utilisé les modules socket et struct de Python
#pour les opérations de réseau et de manipulation de données binaires."
#
# Ajout de l'interface 06-04-2024
# Modif le 08-04-2024
# Modif des couleurs le 09-04-2024
# Mise en modules : UDP.py , UTI.py, LAN.py le 10-04-2024

from tkinter import *
import time
import UDP
import LAN

bg_color = '#048b9a'
fg_color = '#02454d'

WAIT_PACKET = 0.04  # 40 milliseconds


def action():
    NumeroSerie = Z21_LireNumSerie()
    if NumeroSerie is not None:
        global vartext
        vartext = str(NumeroSerie)
        result = Label(master, text = vartext, font = 'arial 12 bold', bg = '#048b9a', fg = 'red')
        result.grid(row=1, column=1)
        print(vartext)
        print("Numéro de série est", NumeroSerie)
    else:
        print("Erreur dans la fonction Z21_LireNumSerie()")
    

def Z21_LireNumSerie():
    NumeroSerie = 0
    LAN.LAN_GET_SERIAL_NUMBER()
    time.sleep(WAIT_PACKET)  # Attente 40ms pour avoir la réponse.
    return LAN.LAN_GET_SERIAL_NUMBER_RESP()


if __name__ == "__main__":
    global socketptr
    UDP.UDP_Initialisation()
    
    master = Tk()
    master.geometry('350x100')
    master.title('INTERFACE Z21')
    master.configure(bg = '#048b9a')
    #vartext=StringVar()
    global vartext
    vartext = 'xxxxxx'
    titre = Label(master, text = "SERIAL Z21", font = 'arial 24 bold', bg = bg_color, fg = 'red')
    titre.grid(row=0, column=0)
    button = Button(master, text = 'SERIAL NUMBER',
                    bg = '#048b9a',fg = 'red', relief='groove',font = 'arial 12 bold', command=action)
    button.grid(row=1, column=0)
    result = Label(master, text = vartext,bg = '#048b9a',fg = 'red', font = 'arial 12 bold')
    result.grid(row=1, column=1)
    
    master.mainloop()
   
    UDP.UDP_Cloture()
