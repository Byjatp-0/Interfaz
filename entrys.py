import tkinter as tk
import time

def aplicar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto)


ventana = tk.Tk()

ventana.title("Soy una ventana")
ventana.geometry("640x480")



etiqueta = tk.Label(ventana, text="lo de abajo es un entry")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Cambiar texto", command=aplicar_texto)
boton.pack()






ventana.mainloop()