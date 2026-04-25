
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.open_question1()

    def open_question1(self):
        if self.current_window:
            self.current_window.destroy()  # Destroy the previous window
        self.current_window = Toplevel(self.master)
        q1(self.current_window, self)  # Pass the main app instance to question class

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
        self.app.open_question2()  # Calls main app method to open question 2

class q2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 5 + 7?').grid()  # Add your question here
        Button(self.master, text='12', command=self.correct).grid()
        Button(self.master, text='13', command=self.incorrect).grid()

    def correct(self):
        Label(self.master, text='Correct').grid()

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()

def window():
    root = Tk()
    app = QuizApp(root)  # Instantiate the main app
    root.mainloop()

if __name__ == '__main__':
    window()
