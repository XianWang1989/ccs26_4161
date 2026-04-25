
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = None  # Track the current question window
        self.next_question(q1)

    def next_question(self, QuestionClass):
        # Destroy the previous question window if it exists
        if self.question_window is not None:
            self.question_window.destroy()

        # Create a new question window
        self.question_window = Toplevel(self.master)
        QuestionClass(self.question_window, self)

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
        Button(self.master, text='Next Question', command=lambda: self.app.next_question(q2)).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=lambda: self.app.next_question(q2)).grid()

class q2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 4 + 4?').grid()
        self.option_1 = Button(self.master, text='7', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='8', command=self.correct)
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

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
