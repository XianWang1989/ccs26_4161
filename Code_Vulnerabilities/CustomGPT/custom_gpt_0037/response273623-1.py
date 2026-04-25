
from tkinter import *

class QuizWindow:
    def __init__(self, master):
        self.master = master
        self.question_window = Toplevel(self.master)
        self.setup_question_1()

    def setup_question_1(self):
        Label(self.question_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.question_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.question_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Correct').grid()
        Button(self.question_window, text='Next Question', command=self.nextq).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Incorrect').grid()
        Button(self.question_window, text='Next Question', command=self.nextq).grid()

    def nextq(self):
        self.question_window.destroy()  # Destroy the current question window
        self.setup_question_2()  # Set up the next question

    def setup_question_2(self):
        self.question_window = Toplevel(self.master)
        Label(self.question_window, text='What is 4 + 4?').grid()
        # Add options and buttons for question 2 here...

def window():
    root = Tk()
    QuizWindow(root)
    root.mainloop()

if __name__ == '__main__':
    window()
