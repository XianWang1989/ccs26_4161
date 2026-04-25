
from tkinter import *

class Question1:
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
        self.master.destroy()  # Destroy the current window
        new_window = Toplevel()  # Create a new Toplevel window
        Question2(new_window)  # Pass the new window to the next question

class Question2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='Question 2: What is 5 + 5?').grid()
        # Add buttons or logic for second question here

def main_window():
    root = Tk()
    Question1(root)
    root.mainloop()

if __name__ == '__main__':
    main_window()
