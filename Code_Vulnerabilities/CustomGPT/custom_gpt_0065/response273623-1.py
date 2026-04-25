
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.start_quiz()

    def start_quiz(self):
        self.open_question_1()

    def open_question_1(self):
        self.current_window = Toplevel(self.master)
        q1(self.current_window, self)

    def open_question_2(self):
        self.current_window.destroy()  # Destroy the previous window
        self.current_window = Toplevel(self.master)
        q2(self.current_window)

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
        self.disable_options("Correct")

    def incorrect(self):
        self.disable_options("Incorrect")

    def disable_options(self, message):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text=message).grid()
        Button(self.master, text='Next Question', command=self.app.open_question_2).grid()

class q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 4 + 4?').grid()
        # Add additional quiz functionality as needed

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
