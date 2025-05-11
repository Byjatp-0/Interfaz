import tkinter as tk

def mostrar_seleccion():
    print("Opción seleccionada:", variable_control.get())

def cambiar_color():
    color_seleccionado = variable_control.get()
    if color_seleccionado == 1:
        ventana.config(bg="Blue")
    elif color_seleccionado == 2:
        ventana.config(bg="Red")

ventana = tk.Tk()
ventana.title("Botones")




variable_control = tk.IntVar() #para que el boton tenga mas opciones

opcion1 = tk.Radiobutton(ventana, text="Opción 1", variable=variable_control, value=1, command=cambiar_color)

opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=variable_control, value=2, command=cambiar_color)

opcion1.pack()
opcion2.pack()

boton = tk.Button(ventana, text="Mostrar opción", command=mostrar_seleccion)
boton.pack()
ventana.mainloop()