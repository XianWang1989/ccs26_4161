
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None  # To keep track of the current question window
        self.start_question()

    def start_question(self):
        self.create_question_window(q1)

    def create_question_window(self, question_class):
        # Destroy the previous window if it exists
        if self.current_window:
            self.current_window.destroy()
        self.current_window = Toplevel(self.master)
        question_class(self.current_window, self)

class q1:
    def __init__(self, master, quiz_app):
        self.master = master
        self.quiz_app = quiz_app
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self._show_result('Correct')

    def incorrect(self):
        self._show_result('Incorrect')

    def _show_result(self, result_text):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text=result_text).grid()
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        self.quiz_app.create_question_window(q2)

class q2:
    def __init__(self, master, quiz_app):
        self.master = master
        self.quiz_app = quiz_app
        Label(self.master, text='What is 4 + 4?').grid()
        Button(self.master, text='8', command=self.correct).grid()
        Button(self.master, text='7', command=self.incorrect).grid()

    def correct(self):
        Label(self.master, text='Correct').grid()

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
