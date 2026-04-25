
from tkinter import *

class Q1:
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
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        self.master.destroy()  # Close the current window
        root = Tk()  # Create a new root window for the next question
        Q2(root)  # Open the next question
        root.mainloop()

class Q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 4 + 4?').grid()
        # Add buttons and logic for Q2 here

def window():
    root = Tk()
    Q1(root)
    root.mainloop()

if __name__ == '__main__':
    window()
