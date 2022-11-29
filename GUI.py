from tkinter import *
from tkinter import scrolledtext as st
import tkinter.font as tkFont
from lexico import leerAlgoritmoLexico
from sintactico import leerAlgoritmoSintactico

##Start tk and create a window
root =Tk()
# Configuraciones de la ventana
root.title("Analizador de código")
#root.geometry("500x600")
root.resizable(width=True, height=True)

# Titulo
titulo = tkFont.Font(family="Verdana", size=20)
labeltitulo = Label(root, text="Intérprete de Rust", fg="Blue", font=titulo).grid(column=0, row=0, pady=10, padx=50, columnspan=2, sticky="n")

# Etiqueta de ingreso
etiqueta1= tkFont.Font(family="Verdana", size=12)
etiqueta1= Label(root,text="Escribe tu código: ", font=etiqueta1)
etiqueta1.grid(column=0, row=1, pady=2, sticky=W, padx=10)

#Cuadros de texto
entrada1 = st.ScrolledText(root, width=60, height=10)
entrada1.grid(column=0, row=2, columnspan=2)

text_code = st.ScrolledText(root, width=60, height=15)
text_code.grid(column=0, row=7, padx=10, pady=10, columnspan=2)

def lexicoButton():
    result = leerAlgoritmoLexico(entrada1.get(1.0, "end-1c"))
    lineasresultantes = ""
    for line in result:
        lineasresultantes = lineasresultantes + line + "\n"  
    text_code.delete('1.0', END)
    text_code.insert("1.0", lineasresultantes)
    #print(entrada1.get(1.0, "end-1c")) 

def sintacticoButton():
    result = leerAlgoritmoSintactico(entrada1.get(1.0, "end-1c"))
    lineasresultantes = ""
    for line in result:
        if line != None:
            lineasresultantes = lineasresultantes + line + "\n"

    text_code.insert("1.0", lineasresultantes)
    text_code.configure(state="disabled")

def semanticoButton():
    print("SEMANTICO")

#Analizador lexico
lexicoButton = Button(root, text="Léxico",fg="black",  font=("Verdana", 10), command=lexicoButton)
lexicoButton.grid(sticky=W, row=6, column=0, pady=10, padx=10)
#Analizador sintáctico
sintacticoButton = Button(root, text="Sintático", fg="black", font=("Verdana", 10), command=sintacticoButton)
sintacticoButton.grid(row=6, column=0, pady=10, padx=120)
#Analizador Semántico
semanticoButton = Button(root, text="Semántico", fg="black", font=("Verdana", 10), command=semanticoButton)
semanticoButton.grid(sticky=E, row=6, column=0, pady=10)

# show window
root.mainloop()