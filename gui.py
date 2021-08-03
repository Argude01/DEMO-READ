from tkinter import *
from tkinter import ttk 
import database

def mostrar_usuario():
    db_demo = database.MyDatabase()
    db_demo.read_db()
    fila = 0 
    print("FILA: " + str(fila))
    print("RESULTADO Lista - FrontEnd: " + str(database.data))
    for user in database.data:
        registro = user
        print('RESULTADO - FrontEnd: ' + str(fila) + " - " + str(registro))
        title1 = Label(frame_title, 
              text=registro, 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
        title1.place(x=25, y=10)
        fila = fila + 1     
 
window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=120)
frame_title.grid(row=1, column=0)

title = Label(frame_navbar, 
              text="Leer / Read",
              font=("Century Gothic", "14"))
title.place(x=250, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="Resultado - BDD", 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
button_agregar = Button(frame_title, text="Mostrar Usuario", 
                        font=("Century Gothic", "14", "bold"),
                        command=mostrar_usuario)
button_agregar.place(x=25, y=50)


window.mainloop()
