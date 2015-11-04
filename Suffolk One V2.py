from tkinter import *
win = Tk()
v = StringVar()
e = Entry(win,textvariable=v)

def newWindow():
    popup = Toplevel(win)
    lbl = Label(popup,text = "Resturant")
    lbl.pack(side=LEFT, padx=10)
    ent = Entry(popup)
    ent.pack(side=LEFT, padx=10)

b1 = Button(win, command = newWindow, text = "Favourite resturant")
b2 = Button(win, text = "Enter a number")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
win.mainLoop()

