
from tkinter import *

class Question:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")
        self.init_question1()

    def init_question1(self):
        # Initialize Question 1
        self.clear_window()
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def clear_window(self):
        # Clear the current window
        for widget in self.master.winfo_children():
            widget.destroy()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Correct!').grid()
        Button(self.master, text='Next Question', command=self.init_question2).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect!').grid()
        Button(self.master, text='Next Question', command=self.init_question2).grid()

    def init_question2(self):
        # Initialize Question 2
        self.clear_window()
        Label(self.master, text='What is the capital of France?').grid()
        self.option_1 = Button(self.master, text='Berlin', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='Paris', command=self.correct_q2)
        self.option_2.grid()

    def correct_q2(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Correct!').grid()
        # Add further logic for next questions or end

def window():
    root = Tk()
    app = Question(root)
    root.mainloop()

if __name__ == '__main__':
    window()
