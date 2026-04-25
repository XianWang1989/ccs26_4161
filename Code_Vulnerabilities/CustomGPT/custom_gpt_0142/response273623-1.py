
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.current_window = None  # Keep track of the current question window
        self.start_q1()

    def start_q1(self):
        self.open_window(q1(self.master, self))

    def open_window(self, new_window):
        if self.current_window is not None:
            self.current_window.destroy()  # Destroy the previous window
        self.current_window = new_window

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
        self.disable_buttons()
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=self.nextq).grid()

    def incorrect(self):
        self.disable_buttons()
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.nextq).grid()

    def nextq(self):
        self.quiz.open_window(q2(self.master, self.quiz))

    def disable_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

class q2:
    def __init__(self, master, quiz):
        self.master = master
        self.quiz = quiz
        Label(self.master, text='What is the capital of France?').grid()
        self.option_1 = Button(self.master, text='Berlin', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='Paris', command=self.correct)
        self.option_2.grid()

    def correct(self):
        Label(self.master, text='Correct').grid()
        Button(self.master, text='End Quiz', command=self.master.quit).grid()

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='End Quiz', command=self.master.quit).grid()

def window():
    root = Tk()
    Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
