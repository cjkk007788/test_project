from tkinter import *
import random

def drawCircle(x,y,r):
    Canvas.create_oval(x-r,y-r,x+r,y+r,width=2,outline = random.choice(colors))
    if r>= 5:
        drawCircle(x+r//2, y, r//2)
        drawCircle(x-r//2, y, r//2)

colors = ["red","green","blue","black","orange","indigo","violet"]
wSize = 1000
radius = 400

window = Tk()
window.title("원모양의 프렉탈")
canvas = Canvas(window,height=wSize,width=wSize,bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
window.mainloop()