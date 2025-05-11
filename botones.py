import tkinter as tk
import time

def cambiar_texto():
    etiqueta.config(text="Boton pulsado")


ventana = tk.Tk()

ventana.title("Soy una ventana")
ventana.geometry("640x480")

boton = tk.Button(ventana, text= "Pincha aquí perro")
boton.config(fg="green", bg="yellow", font=("Futura", 12))
boton.pack()

etiqueta = tk.Label(ventana, text="hola soy un label")
etiqueta.pack()




boton.config(command=cambiar_texto)




ventana.mainloop()