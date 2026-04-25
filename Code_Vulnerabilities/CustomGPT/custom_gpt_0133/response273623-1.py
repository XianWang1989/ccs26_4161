
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.current_window = master
        self.show_question_1()

    def show_question_1(self):
        # Create the first question
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
        # Destroy the current window before creating the next one
        self.current_window.destroy()
        new_window = Tk()  # Create a new window
        self.show_question_2(new_window)

    def show_question_2(self, master):
        # Create the second question
        self.current_window = master  # Update the current window reference
        Label(self.current_window, text='What is the capital of France?').grid()
        self.option_3 = Button(self.current_window, text='Berlin', command=self.incorrect_q2)
        self.option_3.grid()
        self.option_4 = Button(self.current_window, text='Paris', command=self.correct_q2)
        self.option_4.grid()

    def correct_q2(self):
        self.option_3.config(state=DISABLED)
        self.option_4.config(state=DISABLED)
        Label(self.current_window, text='Correct').grid()
        Button(self.current_window, text='End Quiz', command=self.current_window.destroy).grid()

    def incorrect_q2(self):
        self.option_3.config(state=DISABLED)
        self.option_4.config(state=DISABLED)
        Label(self.current_window, text='Incorrect').grid()
        Button(self.current_window, text='End Quiz', command=self.current_window.destroy).grid()

def window():
    root = Tk()
    Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
