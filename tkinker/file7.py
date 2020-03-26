from tkinter import *

root = Tk()


def leftclick(event):
    print('Left')


def rightclick(event):
    print('Right')


def middleclick(event):
    print('Middle')


frame = Frame(root, height=300, width=250)
frame.bind('<Button-1>', leftclick)
frame.bind('<Button-2>', middleclick)
frame.bind('<Button-3>', rightclick)

frame.pack()

root.mainloop()
