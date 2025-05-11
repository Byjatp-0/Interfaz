import tkinter as tk



ventana = tk.Tk()
ventana.title("Checkbutton")

texto = tk.StringVar(value= "Hola")

print(texto.get())#para este tipo de variables hay que usar el .get() 

#texto.set("Culo")  ##lo modifica
#print(texto.get())

entrada = tk.Entry(ventana, textvariable=texto)
entrada.pack()



decimal = tk.DoubleVar(value=3.11)
control_deslizante  =tk.Scale(ventana, variable=decimal, from_= 0, to=10, resolution=0.01, orient="horizontal")
control_deslizante.pack()


ventana.mainloop()