from tkinter import *
from tkinter import scrolledtext as st
import tkinter.font as tkFont
from lexico import leerAlgoritmoLexico
from sintactico import leerAlgoritmoSintactico

def lexicoButton():
    result = leerAlgoritmoLexico(entrada1.get(1.0, "end-1c"))
    lineasresultantes = ""
    for line in result:
        lineasresultantes = lineasresultantes + line + "\n"
    text_code_lex = st.ScrolledText(root, width=65, height=20)
    text_code_lex.insert("1.0", lineasresultantes)
    text_code_lex.grid(column=0, row=6, padx=10, pady=10, columnspan=2)
    text_code_lex.configure(state="disabled")
    #print(entrada1.get(1.0, "end-1c")) 


def sintacticoButton():
    result = leerAlgoritmoSintactico(entrada1.get(1.0, "end-1c"))
    lineasresultantes = ""
    for line in result:
        if line != None:
            lineasresultantes = lineasresultantes + line + "\n"
    text_code_sin = st.ScrolledText(root, width=65, height=20)
    text_code_sin.insert("1.0", lineasresultantes)
    text_code_sin.grid(column=0, row=6, padx=10, pady=10, columnspan=2)
    text_code_sin.configure(state="disabled")


def semanticoButton():
    print("SEMANTICO")
            

##Start tk and create a window
root =Tk()
# Configuraciones de la ventana
root.title("Analizador de código")
#root.geometry("500x600")
root.resizable(width=True, height=True)



#Variables

###Agregar propiedad font a los labels para cambiar su tamanio y fuente

# Titulo
titulo = tkFont.Font(family="Verdana", size=20)
labeltitulo = Label(root, text="Interprete de Rust", fg="Blue", font=titulo).grid(column=0, row=0, pady=10, padx=50, columnspan=2, sticky="n")

# Etiqueta de ingreso
etiqueta1= tkFont.Font(family="Verdana", size=10)
etiqueta1= Label(root,text="Escribe el algoritmo: ", font=etiqueta1 )
etiqueta1.grid(column=0, row=1, pady=15)

#Cuadro de texto
entrada1 = st.ScrolledText(root, width=40,
        height=20)
entrada1.grid(column=0, row=2, columnspan=2)


#Analizador lexico
lexicoButton = Button(root, text="Léxico",fg="black",  font=("Verdana", 8), command=lexicoButton)
lexicoButton.grid(padx=2, row=1, column=2)
#Analizador sintáctico
sintacticoButton = Button(root, text="Sintático", fg="black", font=("Verdana", 8), command=sintacticoButton)
sintacticoButton.grid(padx=2, column=2, row=2)
#Analizador Semántico
semanticoButton = Button(root, text="Semántico", fg="black", font=("Verdana", 8), command=semanticoButton)
semanticoButton.grid(padx=2, column=2, row=3)

# show window
root.mainloop()