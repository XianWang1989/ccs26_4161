
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = None  # Reference for the current question window
        self.start_question1()

    def start_question1(self):
        self.question_window = Toplevel(self.master)
        self.question_window.title("Question 1")
        Label(self.question_window, text='What is 3 + 3?').grid()
        Button(self.question_window, text='5', command=self.incorrect).grid()
        Button(self.question_window, text='6', command=self.correct).grid()

    def correct(self):
        self.show_feedback("Correct")
        Button(self.question_window, text='Next Question', command=self.start_question2).grid()

    def incorrect(self):
        self.show_feedback("Incorrect")
        Button(self.question_window, text='Next Question', command=self.start_question2).grid()

    def show_feedback(self, feedback):
        Label(self.question_window, text=feedback).grid()

    def start_question2(self):
        self.question_window.destroy()  # Destroy the previous question window
        self.question_window = Toplevel(self.master)  # Create a new window for question 2
        self.question_window.title("Question 2")
        Label(self.question_window, text='Question 2').grid()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
