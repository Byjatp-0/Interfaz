import tkinter as tk


def on_click(event):
    print("Boton presionado")

def on_key_press(event):
    if event.char == 'p':
        print("Tecla 'p' presionada")

def on_mouse_move(event):
    print(f"Ratón movido a {event.x}, {event.y}")
ventana = tk.Tk()

ventana.title("Soy una ventana")
ventana.geometry("640x480")


boton = tk.Button(ventana, text="Click")
boton.pack()



boton.bind("<Button-1>", on_click)
ventana.bind("<KeyPress>", on_key_press)
ventana.bind("<Motion>", on_mouse_move)
ventana.mainloop()