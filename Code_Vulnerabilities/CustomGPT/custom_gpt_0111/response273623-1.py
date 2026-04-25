
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = master
        self.create_question1()

    def create_question1(self):
        Label(self.question_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.question_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.question_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Correct').grid()
        Button(self.question_window, text='Next Question', command=self.next_question).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Incorrect').grid()
        Button(self.question_window, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        # Destroy the current question window
        self.question_window.destroy()
        # Create a new window for the next question
        new_window = Toplevel()
        q2(new_window)

class q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 4 + 4?').grid()
        self.option_1 = Button(self.master, text='8', command=self.correct)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='10', command=self.incorrect)
        self.option_2.grid()

    def correct(self):
        Label(self.master, text='Correct').grid()

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
