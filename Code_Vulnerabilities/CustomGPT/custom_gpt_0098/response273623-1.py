
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.next_question(q1)

    def next_question(self, question_class):
        if self.current_window:
            self.current_window.destroy()  # Destroy the previous window
        self.current_window = Toplevel(self.master)
        question_class(self.current_window, self)

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
        self.disable_buttons()
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=lambda: self.app.next_question(q2)).grid()

    def incorrect(self):
        self.disable_buttons()
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=lambda: self.app.next_question(q2)).grid()

    def disable_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

class q2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 2 + 2?').grid()

        self.option_1 = Button(self.master, text='3', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='4', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.disable_buttons()
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=lambda: self.app.next_question(q1)).grid()

    def incorrect(self):
        self.disable_buttons()
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=lambda: self.app.next_question(q1)).grid()

    def disable_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
