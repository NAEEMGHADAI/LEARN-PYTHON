from tkinter import *

root = Tk()


def printName(event):
    print('hello my name is naeem!!!')


button1 = Button(root, text='Print my name', command=printName)
button1.pack()

button2 = Button(root, text='Print my name')
button2.bind("<Button-1>", printName)
button2.pack()

root.mainloop()
