from tkinter import *

#En esta parte definimos la ventana de un examen de tipo real
class interfaz1():

 def newwin2():
     from metodos import verPartidos
     R = Toplevel()
     R.title("Torneos Ecuavoley")
     R.geometry("700x500")
     R.configure(background="red")
     botonAgregar = Button(R, text="Agregar Partido").place(x=50, y=200)
     botonVer = Button(R, text="Ver Partido",command=verPartidos).place(x=50, y=250)
     R.mainloop()

 ventana = Tk()
 colorFondo="#002"
 ventana.title("Torneos Ecuavoley")
 ventana.geometry("700x500")
 ventana.configure(background = colorFondo)
 botonIngreso=Button(ventana, text="Ingresar",command=newwin2).place(x=325,y=300)
 ventana.mainloop()

