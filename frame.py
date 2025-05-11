import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi ventana")

ventana.geometry("620x480")

frame1 = tk.Frame(ventana)
frame1.configure(width=320, height=210, bg="red", bd=5)

boton = tk.Button(frame1, text="hola")
















boton.pack()
frame1.pack()
ventana.mainloop()
