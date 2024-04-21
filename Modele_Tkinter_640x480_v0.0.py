# Modele Tkinter du 21 avril 2024

import customtkinter

app = customtkinter.CTk()
app.geometry("640x480")
app.title("CTk example")
customtkinter.set_default_color_theme("blue")
# Themes: "blue" (standard), "green", "dark-blue"

my_font = customtkinter.CTkFont(family="<arial>", size=24)
big_font = customtkinter.CTkFont(family="<arial>", size=48)

def button_event():
    textbox.delete("0.0", "end")
    textbox.insert("0.0", "123456")

label = customtkinter.CTkLabel(app, font=big_font, text="Z21 & PYTHON", text_color="#00bfff", fg_color="transparent")
label.pack(padx=20,pady=20)

textbox = customtkinter.CTkTextbox(app, font=my_font, width=200)
textbox.insert("0.0", "XXXXXX")  # insert at line 0 character 0
textbox.pack(padx=20,pady=20)

button = customtkinter.CTkButton(app, font=my_font, text="SERIAL NUMBER", command=button_event)
button.pack(padx=20,pady=20)


app.mainloop()