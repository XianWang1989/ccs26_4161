
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.start_question_1()

    def start_question_1(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = Toplevel(self.master)
        q1(self.current_window, self)

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
        self.display_result('Correct')

    def incorrect(self):
        self.display_result('Incorrect')

    def display_result(self, message):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text=message).grid()
        Button(self.master, text='Next Question', command=self.nextq).grid()

    def nextq(self):
        if self.app.current_window:
            self.app.current_window.destroy()
        self.app.current_window = Toplevel(self.app.master)
        q2(self.app.current_window, self.app)

class q2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 2 + 2?').grid()
        Button(self.master, text='4', command=self.correct).grid()
        Button(self.master, text='5', command=self.incorrect).grid()

    def correct(self):
        Label(self.master, text='Correct').grid()

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
