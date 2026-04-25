
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.create_question_1()

    def create_question_1(self):
        self.question_window = Frame(self.master)
        self.question_window.pack()

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
        self.create_question_2()  # Create the next question

    def create_question_2(self):
        self.question_window = Frame(self.master)
        self.question_window.pack()

        Label(self.question_window, text='Question 2: What is 5 + 5?').grid()
        Button(self.question_window, text='10', command=self.correct_q2).grid()
        Button(self.question_window, text='11', command=self.incorrect_q2).grid()

    def correct_q2(self):
        Label(self.question_window, text='Correct').grid()

    def incorrect_q2(self):
        Label(self.question_window, text='Incorrect').grid()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
