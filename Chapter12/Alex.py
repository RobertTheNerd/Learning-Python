from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)

canvas.create_rectangle(15, 15, 350, 350, fill="white")
canvas.pack()

tk.mainloop()