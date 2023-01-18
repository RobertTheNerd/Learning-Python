from tkinter import *


def hello():
    print('hello')


tk = Tk()
btn = Button(tk, text="Click Me", command=hello)
btn.pack()
tk.update()


tk.mainloop()
