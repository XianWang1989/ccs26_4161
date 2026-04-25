
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.show_question1()

    def show_question1(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = Toplevel(self.master)
        q1(self.current_window, self)

class q1:
    def __init__(self, master, quiz):
        self.master = master
        self.quiz = quiz
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
        self.quiz.show_question2()

class q2:
    def __init__(self, master, quiz):
        self.master = master
        self.quiz = quiz
        Label(self.master, text='What is 2 + 2?').grid()
        Button(self.master, text='3', command=self.incorrect).grid()
        Button(self.master, text='4', command=self.correct).grid()

    def correct(self):
        Label(self.master, text='Correct').grid()

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()

def window():
    root = Tk()
    Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
