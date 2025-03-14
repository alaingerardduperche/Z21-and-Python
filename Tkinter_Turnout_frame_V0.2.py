#################################################
# Tkinter Python & Z21
#
# Alain Duperche Avril 2024
################################################"
# Import the library tkinter 
from tkinter import *

app = Tk() 
app.geometry("640x400")

def quitt():
    app.destroy()

def droit():
    canvas.create_image(80, 50, image=logo_d)
    print(droit)
    
def courbe():
    canvas.create_image(80, 50, image=logo_c)
    print(courbe)

# Constructing the frame1 
frame1 = LabelFrame(app, text="Fruit", bg="green",fg="white", padx=15, pady=15) 
frame1.grid(row=0, column=0) 
b1 = Button(frame1, text="Quitter", command = quitt).grid(row=0,column=0) 
b2 = Button(frame1, text="DROIT", command = droit).grid(row=0,column=1)
b3 = Button(frame1, text="COURBE", command = courbe).grid(row=0,column=2)


# Constructing Canvas
logo = PhotoImage(file="turnout.gif")
logo_d = PhotoImage(file="turnout_Vert.gif")
logo_c = PhotoImage(file="turnout_rouge.gif")
canvas = Canvas(app, bg="blue")
canvas.grid(row=1, column=0)
canvas.create_image(80, 50, image=logo)

# Make the loop for displaying app 
app.mainloop() 