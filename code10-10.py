from tkinter import*

def drawCircle(x,y,r):
    global count
    count = count+1

    Canvas.create_oval(x-r,y-r,x+r,y+r)
    Canvas.create_text(x,y-r,text=str(count),font=('',30))
    if r >= radius/2:
        drawCircle(x-r//2,y,r//2)
        drawCircle(x+r//2,y,r//2)
        
    
count = 0
wSize = 1000
radius = 400


window = Tk()
canvas = Canvas(window,height=wSize,width = wSize,bg='white')

drawCircle(wSize//2,wSize//2,radius)

Canvas.pack()
window.mainloop()