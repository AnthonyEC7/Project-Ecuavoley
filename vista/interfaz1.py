from tkinter import *

#En esta parte definimos la ventana de un examen de tipo real
def newwin2():
    R = Toplevel()
    R.title("Torneos Ecuavoley")
    R.geometry("700x500")
    R.configure(background=colorFondo)
    botonAgregar = Button(R, text="Agregar Partido").place(x=50, y=200)
    botonVer = Button(R, text="Ver Partido").place(x=50, y=250)
    R.mainloop()

ventana = Tk()
colorFondo="#002"
ventana.title("Torneos Ecuavoley")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)
botonIngreso=Button(ventana, text="Ingresar",command=newwin2).place(x=325,y=300)
ventana.mainloop()

