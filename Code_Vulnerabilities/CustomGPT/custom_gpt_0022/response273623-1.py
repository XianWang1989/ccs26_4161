
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.create_question_one()

    def create_question_one(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = Toplevel(self.master)

        Label(self.current_window, text='What is 3 + 3?').grid()
        Button(self.current_window, text='5', command=self.incorrect).grid()
        Button(self.current_window, text='6', command=self.correct).grid()

    def correct(self):
        self.show_feedback('Correct')

    def incorrect(self):
        self.show_feedback('Incorrect')

    def show_feedback(self, message):
        Label(self.current_window, text=message).grid()
        Button(self.current_window, text='Next Question', command=self.create_question_two).grid()

    def create_question_two(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = Toplevel(self.master)

        Label(self.current_window, text='Question 2: What is 2 + 2?').grid()
        Button(self.current_window, text='3', command=self.incorrect).grid()
        Button(self.current_window, text='4', command=self.correct_two).grid()

    def correct_two(self):
        self.show_feedback('Correct')

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
