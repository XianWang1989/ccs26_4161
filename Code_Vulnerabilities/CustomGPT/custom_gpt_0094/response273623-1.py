
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.show_question_1()

    def show_question_1(self):
        self.destroy_current_window()
        self.current_window = Toplevel(self.master)

        Label(self.current_window, text='What is 3 + 3?').grid()
        Button(self.current_window, text='5', command=self.incorrect).grid()
        Button(self.current_window, text='6', command=self.correct).grid()

    def correct(self):
        self.show_result('Correct', self.show_question_2)

    def incorrect(self):
        self.show_result('Incorrect', self.show_question_2)

    def show_result(self, message, next_question_func):
        Label(self.current_window, text=message).grid()
        Button(self.current_window, text='Next Question', command=next_question_func).grid()

    def show_question_2(self):
        self.destroy_current_window()
        self.current_window = Toplevel(self.master)

        Label(self.current_window, text='What is 4 + 4?').grid()
        Button(self.current_window, text='7', command=self.incorrect).grid()
        Button(self.current_window, text='8', command=self.correct).grid()

    def destroy_current_window(self):
        if self.current_window is not None:
            self.current_window.destroy()
            self.current_window = None

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
