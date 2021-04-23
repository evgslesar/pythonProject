# -*- coding: utf-8 -*-
import time
from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

mytriangle = canvas.create_polygon(10,10, 10,60, 50,35, fill='red')
def movetriange(event):
    if event.keysym == 'Up':
        canvas.move(mytriangle, 0, -3)
        canvas.itemconfig(mytriangle, fill='green')
    elif event.keysym == 'Down':
        canvas.move(mytriangle, 0, 3)
        canvas.itemconfig(mytriangle, fill='yellow')
    elif event.keysym == 'Left':
        canvas.move(mytriangle, -3, 0)
        canvas.itemconfig(mytriangle, fill='blue')
    else:
        canvas.move(mytriangle, 3, 0)
        canvas.itemconfig(mytriangle, fill='cyan')

canvas.bind_all('<KeyPress-Up>', movetriange)
canvas.bind_all('<KeyPress-Down>', movetriange)
canvas.bind_all('<KeyPress-Left>', movetriange)
canvas.bind_all('<KeyPress-Right>', movetriange)

tk.mainloop()

