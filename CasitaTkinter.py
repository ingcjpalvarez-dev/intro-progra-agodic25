import tkinter as tk

ventana = tk.Tk()
ventana.title("Casita tkinter")
ventana.geometry("500x500")

lienzo = tk.Canvas(ventana, width=500, height=500, bg="light blue")
lienzo.pack()

# Césped
lienzo.create_rectangle(0, 300, 500, 500, fill="green", outline="")

# Casa principal
lienzo.create_rectangle(180, 200, 320, 350, fill="orange")

# Techo especial
lienzo.create_polygon(160, 200, 340, 200, 320, 150, 180, 150, fill="purple")

# Puerta azul
lienzo.create_rectangle(230, 270, 270, 350, fill="blue")

# Ventana cuadriculada
lienzo.create_rectangle(190, 220, 220, 250, fill="yellow")
lienzo.create_line(205, 220, 205, 250, width=2)
lienzo.create_line(190, 235, 220, 235, width=2)

# Camino de piedras
lienzo.create_rectangle(230, 350, 270, 450, fill="gray")
lienzo.create_oval(225, 370, 240, 385, fill="white")
lienzo.create_oval(255, 390, 270, 405, fill="white")
lienzo.create_oval(240, 420, 255, 435, fill="white")
lienzo.create_oval(210, 400, 245, 425, fill="white"  )
# Nube
lienzo.create_oval(350, 80, 400, 100, fill="white", outline="")
lienzo.create_oval(370, 70, 420, 90, fill="white", outline="")
lienzo.create_oval(390, 80, 440, 100, fill="white", outline="")

ventana.mainloop()