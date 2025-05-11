import tkinter as tk
import time

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_hora)



ventana = tk.Tk()

ventana.title("Reloj supremo")
ventana.geometry("640x480")

etiqueta = tk.Label(ventana, text= "")
etiqueta.pack()

actualizar_hora()

ventana.mainloop()