
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.create_question1()

    def create_question1(self):
        self.clear_window()
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=self.create_question2).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.create_question2).grid()

    def create_question2(self):
        self.clear_window()
        Label(self.master, text='Question 2: What is 5 + 5?').grid()
        self.option_1 = Button(self.master, text='10', command=self.correct_q2)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='11', command=self.incorrect_q2)
        self.option_2.grid()

    def correct_q2(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Correct').grid()

    def incorrect_q2(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
