from tkinter import *

root = Tk()

topframe = Frame(root)
topframe.pack()
bootomframe = Frame(root)
bootomframe.pack(side=BOTTOM)

button = Button(topframe, text='button 1', fg='red')
button2 = Button(topframe, text='button 2', fg='blue')
button3 = Button(topframe, text='button 3', fg='green')
button4 = Button(bootomframe, text='button 4', fg='purple')

button.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()


root.mainloop()
