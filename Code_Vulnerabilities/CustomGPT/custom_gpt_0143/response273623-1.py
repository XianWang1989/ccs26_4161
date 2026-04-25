
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = None
        self.start_question_1()

    def start_question_1(self):
        self.question_window = Toplevel(self.master)
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
        self.question_window.destroy()  # Destroy the current question window
        self.start_question_2()

    def start_question_2(self):
        self.question_window = Toplevel(self.master)
        Label(self.question_window, text='What is 4 + 4?').grid()
        Button(self.question_window, text='7', command=self.incorrect_q2).grid()
        Button(self.question_window, text='8', command=self.correct_q2).grid()

    def correct_q2(self):
        Label(self.question_window, text='Correct').grid()

    def incorrect_q2(self):
        Label(self.question_window, text='Incorrect').grid()

def run_quiz():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    run_quiz()
