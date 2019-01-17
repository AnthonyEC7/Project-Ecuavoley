import tkinter
from tkinter import *
from tkinter import messagebox


def saludar():
    if nombre.get()=="" and lugar.get()=="" and fecha.get()=="":
        messagebox.showinfo(title="error", message="Ingrese al menos un campo")
    else:
        messagebox.showinfo(message="INFORMACION \n" +"NOMBRE DE LA CANCHA: " +nombre.get() +"\n"+ "LUGAR DE LA CANCHA: " + lugar.get()+"\n" + "FECHA RESERVA: " + fecha.get())

ventana = Tk()
nombre = StringVar()
lugar = StringVar()
fecha = StringVar()

ventana.title("Entrads en tkinder")
ventana.geometry("400x400")
etiqueta1 = Label(ventana, text="Ingrese nombre de la cancha").place(x=10, y=10)
nombreCaja = Entry(ventana, textvariable=nombre).place(x=170, y=10)
etiqueta2 = Label(ventana, text="Escribre lugar").place(x=10, y=40)
apellidoPCaja = Entry(ventana, textvariable=lugar).place(x=170, y=40)
etiqueta3 = Label(ventana, text="Escribre tu fecha").place(x=10, y=70)
apellidoMCaja = Entry(ventana, textvariable=fecha).place(x=170, y=70)
boton = Button(ventana, text="GUARDAR ", command=saludar).place(y=90), ventana.mainloop()
