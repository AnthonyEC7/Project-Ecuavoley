from fileinput import filename
from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("RESERVA DE PARTIDOS ECUAVOLEY")
ecuavoley = StringVar()




def verPartidos():
    infile = open("PARTIDOS.txt", "r")
    textfield.insert(INSERT,infile.readlines())
    infile.close()

def agregarPartidos():
    root.iconify()
    global ventana
    ventana = Tk()
    nombre1 = StringVar()
    nombre2 = StringVar()
    nombre3 = StringVar()
    nombre4 = StringVar()
    nombre5 = StringVar()
    nombre6 = StringVar()
    monto = StringVar()
    colorFondo = "#002"
    ventana.title("Torneos Ecuavoley")
    ventana.geometry("700x500")
    ventana.configure(background=colorFondo)
    etiquet = Label(ventana, text="Equipo 1").place(x=125, y=10)
    etiqueta = Label(ventana, text="Jugador 1").place(x=10,y=40)
    caja1 = Entry(ventana, textvariable=nombre1).place(x=100,y=40)
    etiqueta1 = Label(ventana, text="Jugador 2").place(x=10, y=70)
    caja2 = Entry(ventana, textvariable=nombre2).place(x=100, y=70)
    etiqueta2 = Label(ventana, text="Jugador 3").place(x=10, y=100)
    caja3 = Entry(ventana, textvariable=nombre3).place(x=100, y=100)
    etique = Label(ventana, text="VS").place(x=290, y=70)
    etiqueta3 = Label(ventana, text="Equipo 2").place(x=500, y=10)
    etiqueta = Label(ventana, text="Jugador 1").place(x=375, y=40)
    caja4 = Entry(ventana, textvariable=nombre4).place(x=475, y=40)
    etiqueta4 = Label(ventana, text="Jugador 2").place(x=375, y=70)
    caja5 = Entry(ventana, textvariable=nombre5).place(x=475, y=70)
    etiqueta5 = Label(ventana, text="Jugador 3").place(x=375, y=100)
    caja6 = Entry(ventana, textvariable=nombre6).place(x=475, y=100)
    etiqueta6 = Label(ventana, text="Monto").place(x=375, y=200)
    caja7 = Entry(ventana, textvariable=monto).place(x=475, y=200)
    boton1 = Button(ventana, text="<-- Regresar",command=regresar).place(x=100, y=450)
    boton2 = Button(ventana, text="-- Guardar --",command=regresar).place(x=475, y=450)

def regresar():

    root.deiconify()
    ventana.iconify()


btnVerPartidos = Button(root, text="Ver Partidos", command=verPartidos).grid(row=1, column=0)
btnAgregar = Button(root, text="Agregar Partidos", command=agregarPartidos).grid(row=2, column=0)

textfield = Text(root)
textfield.grid(row=1, column=1, rowspan=2)
root.mainloop()








