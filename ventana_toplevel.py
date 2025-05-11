import tkinter as tk

def abrir_ventana_toplevel():
    toplevel1 = tk.Toplevel(ventana)
    toplevel1.title("Ventana toplevel")
    toplevel1.geometry("180x100")
    label1 = tk.Label(toplevel1, text="Ventana toplevel")
    label1.pack()


ventana = tk.Tk()
ventana.title("Ventana principal")
ventana.geometry("640x480")


boton = tk.Button(ventana, text="Abrir ventana toplevel", command=abrir_ventana_toplevel)
boton.pack()
ventana.mainloop()