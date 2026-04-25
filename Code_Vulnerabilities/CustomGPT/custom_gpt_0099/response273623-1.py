
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = None
        self.start_question_1()

    def start_question_1(self):
        self.create_question_window(q1)

    def create_question_window(self, question_class):
        if self.question_window is not None:
            self.question_window.destroy()  # Destroy the previous window

        self.question_window = Toplevel(self.master)
        question_class(self.question_window)

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
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        app.create_question_window(q2)

class q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is the capital of France?').grid()
        Button(self.master, text='Paris', command=self.correct).grid()
        Button(self.master, text='London', command=self.incorrect).grid()

    def correct(self):
        Label(self.master, text='Correct!').grid()

    def incorrect(self):
        Label(self.master, text='Incorrect!').grid()

def window():
    root = Tk()
    global app
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
