from tkinter import *

root = Tk()

one = Label(root, text='ONE', fg='red', bg='white')
one.pack()
two = Label(root, text='TWO', fg='green', bg='black')
two.pack(fill=X)
three = Label(root, text='THREE', fg='blue', bg='white')
three.pack(side=LEFT, fill=Y)

root.mainloop()
