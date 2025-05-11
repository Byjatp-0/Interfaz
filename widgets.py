import tkinter as tk

def cuenta_regresiva(valor):
    if valor > 0:
        etiqueta.config(text=str(valor))
        ventana.after(1000, cuenta_regresiva, valor - 1)  
    else:
        etiqueta.config(text="Hola")

ventana = tk.Tk()
ventana.geometry("640x480")
ventana.title("Ejemplo widgets")

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

cuenta_regresiva(3)  

ventana.mainloop()

