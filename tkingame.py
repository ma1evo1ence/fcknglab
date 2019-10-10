from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg = 'white')
canv.pack(fill = BOTH,expand = 1)

colors = ['red','orange','yellow','green','blue']
k = 0



def new_ball():
    global x, y, r
    canv.delete("ball")
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r , x + r, y + r, fill = choice(colors), width = 0, tag = "ball")
    root.after(1000, new_ball)
    canv.create_rectangle(50, 80, 150, 120, fill="cyan")
    canv.create_text(100, 100, text = ("Score:", k), justify=CENTER, font = "Impact 16")


def click(event):
    global k
    if (event.x - x) * (event.x - x) + (event.y - y) * (event.y - y) <= r * r:
        k += 1
        print(k)

new_ball()
print(k)
canv.bind('<Button-1>', click)
mainloop()
