
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.current_window = self.master
        self.create_question_1()

    def create_question_1(self):
        Label(self.current_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_window, text='Correct!').grid()
        Button(self.current_window, text='Next Question', command=self.create_question_2).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_window, text='Incorrect!').grid()
        Button(self.current_window, text='Next Question', command=self.create_question_2).grid()

    def create_question_2(self):
        self.current_window.destroy()  # Destroy the previous window
        new_window = Toplevel()  # Create a new Toplevel window
        self.current_window = new_window  # Update reference to the current window
        Label(new_window, text='Question 2: What is 5 + 5?').grid()
        Button(new_window, text='10', command=self.question2_correct).grid()
        Button(new_window, text='11', command=self.question2_incorrect).grid()

    def question2_correct(self):
        Label(self.current_window, text='Correct!').grid()

    def question2_incorrect(self):
        Label(self.current_window, text='Incorrect!').grid()

def main_window():
    root = Tk()
    Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    main_window()
