from tkinter import *

root = Tk()


class BuckysBottons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.printbutton = Button(
            frame, text='Print message', command=self.printbutton)
        self.printbutton.pack(side=LEFT)

        self.printbutton = Button(frame, text='QUIT', command=frame.quit)
        self.printbutton.pack(side=RIGHT)

    def printbutton(self):
        print('WOW,THIS ACTUALLY WOKS!!!')


b = BuckysBottons(root)

root.mainloop()
