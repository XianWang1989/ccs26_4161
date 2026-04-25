
from tkinter import *

class q1:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=self.nextq).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.nextq).grid()

    def nextq(self):
        new_window = Toplevel(self.master)
        self.master.destroy()  # Destroy the previous window
        q2(new_window)

class q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 5 + 5?').grid()
        Button(self.master, text='10', command=self.correct).grid()
        Button(self.master, text='11', command=self.incorrect).grid()

    def correct(self):
        Label(self.master, text='Correct!').grid()

    def incorrect(self):
        Label(self.master, text='Incorrect!').grid()

def window():
    root = Tk()
    q1(root)
    root.mainloop()

if __name__ == '__main__':
    window()
