
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = None  # This will hold the current question window
        self.show_question_1()

    def show_question_1(self):
        self._create_question_window("What is 3 + 3?", 
            [("5", self.incorrect), ("6", self.correct)])

    def show_question_2(self):
        self._create_question_window("What is the capital of France?", 
            [("Berlin", self.incorrect), ("Paris", self.correct)])

    def _create_question_window(self, question, options):
        if self.question_window is not None:
            self.question_window.destroy()  # Close the previous question window
        self.question_window = Toplevel(self.master)
        Label(self.question_window, text=question).grid()
        for text, command in options:
            Button(self.question_window, text=text, command=command).grid()

    def correct(self):
        Label(self.question_window, text='Correct!').grid()
        Button(self.question_window, text='Next Question', command=self.show_question_2).grid()

    def incorrect(self):
        Label(self.question_window, text='Incorrect!').grid()
        Button(self.question_window, text='Next Question', command=self.show_question_2).grid()


def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
