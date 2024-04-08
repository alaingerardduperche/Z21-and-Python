#
from tkinter import *   
  
master = Tk()
master.geometry('350x100')
master.title('INTERFACE Z21')
    
# Create widgets

vartext=StringVar()
vartext.set('xxxxxxxxxxxx')
titre = Label(master, text = "Z21", font = 'arial 24')
titre.grid(row=0, column=2)
button = Button(master, text = 'SERIAL NUMBER', bg='#aa8888', relief='groove', font = 'arial 12')
button.grid(row=1, column=0)
result = Label(master, textvariable = vartext, font = 'arial 12', relief = RAISED)
result.grid(row=1, column=3)
  
master.mainloop() 