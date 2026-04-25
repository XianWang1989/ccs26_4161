
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = self.master  # Keep track of the current window
        self.question_1()

    def question_1(self):
        Label(self.current_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_window, text='Correct').grid()
        Button(self.current_window, text='Next Question', command=self.next_question).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_window, text='Incorrect').grid()
        Button(self.current_window, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        new_window = Toplevel(self.master)
        self.current_window.destroy()  # Destroy the current window
        self.current_window = new_window  # Update the reference to the current window
        self.question_2()

    def question_2(self):
        Label(self.current_window, text='Question 2').grid()

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
