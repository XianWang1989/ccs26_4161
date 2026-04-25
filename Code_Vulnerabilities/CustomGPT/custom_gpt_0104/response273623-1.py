
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = None  # Store the current question window
        self.show_question_1()

    def show_question_1(self):
        if self.question_window:
            self.question_window.destroy()  # Destroy the previous window if it exists
        self.question_window = Toplevel(self.master)
        q1(self.question_window, self)

class q1:
    def __init__(self, master, app):
        self.master = master
        self.app = app
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
        self.app.show_question_2()

class q2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 5 + 5?').grid()
        self.option_1 = Button(self.master, text='10', command=self.correct)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='11', command=self.incorrect)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Finish', command=self.master.destroy).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Finish', command=self.master.destroy).grid()

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = None  # Store the current question window
        self.show_question_1()

    def show_question_1(self):
        if self.question_window is not None:
            self.question_window.destroy()
        self.question_window = Toplevel(self.master)
        q1(self.question_window, self)

    def show_question_2(self):
        if self.question_window is not None:
            self.question_window.destroy()
        self.question_window = Toplevel(self.master)
        q2(self.question_window, self)

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
