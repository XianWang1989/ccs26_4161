
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = master
        self.open_question_1()

    def open_question_1(self):
        self.current_window.withdraw()  # Hide the current window
        self.window1 = Toplevel(self.master)
        self.question_1 = Question1(self.window1, self)

    def open_question_2(self):
        self.window1.destroy()  # Destroy the first question window
        self.window2 = Toplevel(self.master)
        self.question_2 = Question2(self.window2, self)

class Question1:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.display_feedback("Correct")
        Button(self.master, text='Next Question', command=self.app.open_question_2).grid()

    def incorrect(self):
        self.display_feedback("Incorrect")
        Button(self.master, text='Next Question', command=self.app.open_question_2).grid()

    def display_feedback(self, message):
        Label(self.master, text=message).grid()

class Question2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 4 + 4?').grid()
        Button(self.master, text='8', command=self.correct).grid()
        Button(self.master, text='7', command=self.incorrect).grid()

    def correct(self):
        self.display_feedback("Correct")

    def incorrect(self):
        self.display_feedback("Incorrect")

    def display_feedback(self, message):
        Label(self.master, text=message).grid()

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
