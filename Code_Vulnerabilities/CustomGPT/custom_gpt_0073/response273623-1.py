
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = self.master
        self.show_question_1()

    def show_question_1(self):
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
        self.question_window.destroy()  # Destroy the current window
        new_window = Toplevel(self.master)  # Create a new window for the next question
        QuizQuestion2(new_window)  # Pass the new window to the next question class

class QuizQuestion2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 5 + 5?').grid()
        Button(self.master, text='10', command=self.correct).grid()
        Button(self.master, text='11', command=self.incorrect).grid()

    def correct(self):
        Label(self.master, text='Correct').grid()

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
