
from tkinter import *

class QuestionOne:
    def __init__(self, master):
        self.master = master
        self.label = Label(self.master, text='What is 3 + 3?')
        self.label.grid()
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
        # Destroy the current window
        self.master.destroy()
        # Create a new window for the next question
        next_window = Toplevel()
        QuestionTwo(next_window)

class QuestionTwo:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 5 + 5?').grid()
        Button(self.master, text='10', command=self.next_question).grid()

    def next_question(self):
        Label(self.master, text='Correct!').grid()

def main_window():
    root = Tk()
    QuestionOne(root)
    root.mainloop()

if __name__ == '__main__':
    main_window()
