
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
        # Destroy the current window before creating a new one
        self.master.destroy()
        new_window = Tk()  # Create a new Tk instance for the next question
        q2(new_window)     # Pass the new instance to the next question class

class q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='Question 2').grid()
        Button(self.master, text='Exit', command=self.master.destroy).grid()  # Added an exit button

def window():
    root = Tk()
    q1(root)
    root.mainloop()

if __name__ == '__main__':
    window()
