import tkinter as tk
#los checkbutton sirven para seleccionar varias cosas a la vez 
def on_checkbutton_cambio():
    if variable_check1.get():
        boton.config(state="active")
    else:
        boton.config(state="disabled")

ventana = tk.Tk()
ventana.title("Checkbutton")

variable_check1 = tk.BooleanVar()



check1 = tk.Checkbutton(ventana, text="Habilitar botón", variable=variable_check1, command=on_checkbutton_cambio)



check1.pack()
boton = tk.Button(ventana, text="Botón", state="disabled")
boton.pack()

ventana.mainloop()