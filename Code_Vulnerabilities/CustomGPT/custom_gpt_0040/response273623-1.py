
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.show_question_1()

    def show_question_1(self):
        self.create_window("What is 3 + 3?", [("5", self.incorrect), ("6", self.correct)])

    def create_window(self, question, options):
        if self.current_window:
            self.current_window.destroy()  # Destroy the previous window

        self.current_window = Toplevel(self.master)
        Label(self.current_window, text=question).grid()

        for text, command in options:
            Button(self.current_window, text=text, command=command).grid()

    def correct(self):
        self.create_result_window("Correct", self.show_question_2)

    def incorrect(self):
        self.create_result_window("Incorrect", self.show_question_2)

    def create_result_window(self, message, next_question_func):
        self.create_window(message, [])
        Button(self.current_window, text='Next Question', command=next_question_func).grid()

    def show_question_2(self):
        self.create_window("What is 2 + 2?", [("3", self.incorrect), ("4", self.correct)])

def main():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
