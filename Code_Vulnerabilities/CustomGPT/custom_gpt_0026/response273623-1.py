
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.start_quiz()

    def start_quiz(self):
        self.open_question_1()

    def open_question_1(self):
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
        self.disable_buttons()
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=self.app.open_question_2).grid()

    def incorrect(self):
        self.disable_buttons()
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.app.open_question_2).grid()

    def disable_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

class q2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 5 + 5?').grid()
        Button(self.master, text='10', command=self.correct).grid()
        Button(self.master, text='11', command=self.incorrect).grid()

    def correct(self):
        Label(self.master, text='Correct').grid()
        # You can add logic to go to the next question or finish

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()
        # You can add logic to go to the next question or finish

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
