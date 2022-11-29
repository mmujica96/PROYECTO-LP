from tkinter import *
from tkinter import scrolledtext as st
import tkinter.font as tkFont

def lexicoButton():
    print("LEXICO " + algoritmo.get()) 
def sintacticoButton():
    print("SINTACTICO")
def semanticoButton():
    print("SEMANTICO")
            

##Start tk and create a window
root =Tk()
# Configuraciones de la ventana
root.title("Analizador de código")
root.geometry("400x300")
root.resizable(width=True, height=True)



#Variables
algoritmo = StringVar()
algoritmo.set("Algoritmo a evaluar")

###Agregar propiedad font a los labels para cambiar su tamanio y fuente

# Titulo
titulo = tkFont.Font(family="Lucia Grande", size=20)
labeltitulop = Label(root, text="Interprete de Rust", fg="Blue", font=titulo).grid(column=0, row=0, pady=10, padx=50, columnspan=2)

# Etiqueta de ingreso
etiqueta1= tkFont.Font(family="Lucida Grande", size=10)
etiqueta1= Label(root,text="Escribe el algoritmo: ", font=etiqueta1 )
etiqueta1.place(x=20, y=80)

#Cuadro de texto
entrada1 = Entry(root, textvariable=algoritmo)
entrada1.place(x=20, y=100, width=300,
        height=100)


#Analizador lexico
lexicoButton = Button(root, text="Léxico", command=lexicoButton)
lexicoButton.place(x=330, y=100)
#Analizador sintáctico
sintacticoButton = Button(root, text="Sintático", command=sintacticoButton)
sintacticoButton.place(x=330, y=140)
#Analizador Semántico
semanticoButton = Button(root, text="Semántico", command=semanticoButton)
semanticoButton.place(x=330, y=180)

# show window
root.mainloop()