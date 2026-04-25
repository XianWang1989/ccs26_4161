
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.show_question_1()

    def show_question_1(self):
        # Destroy previous window if it exists
        if self.current_window:
            self.current_window.destroy()

        self.current_window = Toplevel(self.master)
        Label(self.current_window, text='What is 3 + 3?').grid()
        Button(self.current_window, text='5', command=self.incorrect).grid()
        Button(self.current_window, text='6', command=self.correct).grid()

    def correct(self):
        Label(self.current_window, text='Correct').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def incorrect(self):
        Label(self.current_window, text='Incorrect').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def show_question_2(self):
        self.show_question_1()  # Call to show the next question

    def nextq(self):
        pass  # Implement additional functionality for the next question as needed

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
