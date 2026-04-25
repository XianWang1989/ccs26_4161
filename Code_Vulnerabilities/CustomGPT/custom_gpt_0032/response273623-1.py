
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.show_question_1()

    def show_question_1(self):
        self.question1_window = Toplevel(self.master)
        Label(self.question1_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.question1_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.question1_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.disable_buttons()
        Label(self.question1_window, text='Correct').grid()
        Button(self.question1_window, text='Next Question', command=self.show_question_2).grid()

    def incorrect(self):
        self.disable_buttons()
        Label(self.question1_window, text='Incorrect').grid()
        Button(self.question1_window, text='Next Question', command=self.show_question_2).grid()

    def disable_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

    def show_question_2(self):
        self.question1_window.destroy()  # Destroy the previous window
        self.question2_window = Toplevel(self.master)
        Label(self.question2_window, text='Question 2: What is 5 + 5?').grid()
        Button(self.question2_window, text='10', command=self.question2_correct).grid()
        Button(self.question2_window, text='11', command=self.question2_incorrect).grid()

    def question2_correct(self):
        Label(self.question2_window, text='Correct!').grid()

    def question2_incorrect(self):
        Label(self.question2_window, text='Incorrect!').grid()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
