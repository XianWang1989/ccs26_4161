
from tkinter import *

class Q1:
    def __init__(self, master):
        self.master = master
        self.question_window = master  # Store reference to the current window
        Label(self.question_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.question_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.question_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Correct').grid()
        Button(self.question_window, text='Next Question', command=self.nextq).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Incorrect').grid()
        Button(self.question_window, text='Next Question', command=self.nextq).grid()

    def nextq(self):
        self.question_window.destroy()  # Destroy the current window
        new_window = Toplevel(self.master)  # Create a new Toplevel window
        Q2(new_window)  # Pass the new window to the next question

class Q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='Question 2').grid()

def window():
    root = Tk()
    Q1(root)
    root.mainloop()

if __name__ == '__main__':
    window()
