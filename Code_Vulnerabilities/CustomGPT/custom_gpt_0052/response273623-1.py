
from tkinter import *

class Quiz:
    def __init__(self):
        self.root = Tk()
        self.current_window = None
        self.next_question(q1)

    def next_question(self, question_class):
        if self.current_window is not None:
            self.current_window.destroy()
        self.current_window = Toplevel(self.root)
        question_class(self.current_window, self)

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
        Button(self.master, text='Next Question', command=lambda: self.quiz.next_question(q2)).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=lambda: self.quiz.next_question(q2)).grid()

class q2:
    def __init__(self, master, quiz):
        self.master = master
        self.quiz = quiz
        Label(self.master, text='What is 4 + 4?').grid()
        Button(self.master, text='8', command=self.correct).grid()
        Button(self.master, text='9', command=self.incorrect).grid()

    def correct(self):
        Label(self.master, text='Correct').grid()

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()

def main():
    quiz = Quiz()
    quiz.root.mainloop()

if __name__ == '__main__':
    main()
