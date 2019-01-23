


from tkinter import *



def verPartidos():
    infile = open("encuentro.txt", "r")
    textfield.insert(INSERT,infile.readlines())
    infile.close()

def agregarPartidos():

    agregar = Toplevel(root)
    root.iconify()


root = Tk()
root.title("RESERVA DE PARTIDOS ECUAVOLEY")
ecuavoley = StringVar()
label1 = Label(root, text="CANCHA LA LOMA").grid(row=0, column=0)

btnverPartidos = Button(root, text="Ver Partidos", command=verPartidos).grid(row=2, column=0)
btnagregarPartidos = Button(root, text="Agregar Partido", command=agregarPartidos).grid(row=1, column=0)
textfield = Text(root)
textfield.grid(row=1, column=1, rowspan=2)
root.mainloop()








