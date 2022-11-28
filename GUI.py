from tkinter import *
##Clase ventana
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        ###Agregar propiedad font a los labels para cambiar su tamanio y fuente
        #Analizador lexico
        lexicoButton = Button(self, text="Léxico", command=self.lexicoButton)
        lexicoButton.place(x=0, y=20)
        #Analizador sintáctico
        sintacticoButton = Button(self, text="Sintático", command=self.sintacticoButton)
        sintacticoButton.place(x=60, y=20)
        #Analizador Semántico
        semanticoButton = Button(self, text="Semántico", command=self.semanticoButton)
        semanticoButton.place(x=130, y=20)

        text = Label(self, text="Botones juas")
        text.place(x=0,y=0)

    ##metodos que usa la clase Window

    def lexicoButton(self):
        print("LEXICO")
    def sintacticoButton(self):
        print("SINTACTICO")
    def semanticoButton(self):
        print("SEMANTICO")
            

##Start tk and create a window
root = Tk()
app = Window(root)

# Configuraciones de la ventana
root.wm_title("Analizador de código")
root.geometry("640x400")

# show window
root.mainloop()