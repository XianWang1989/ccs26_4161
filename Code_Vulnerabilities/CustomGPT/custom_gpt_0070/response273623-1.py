
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.current_question = None
        self.show_question1()

    def show_question1(self):
        if self.current_question:
            self.current_question.destroy()  # Destroy the previous window if it exists
        self.current_question = Frame(self.master)
        self.current_question.grid()
        Label(self.current_question, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_question, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_question, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_question, text='Correct').grid()
        Button(self.current_question, text='Next Question', command=self.show_question2).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_question, text='Incorrect').grid()
        Button(self.current_question, text='Next Question', command=self.show_question2).grid()

    def show_question2(self):
        if self.current_question:
            self.current_question.destroy()
        self.current_question = Frame(self.master)
        self.current_question.grid()
        Label(self.current_question, text='What is the capital of France?').grid()
        self.option_1 = Button(self.current_question, text='Berlin', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_question, text='Paris', command=self.correct)
        self.option_2.grid()

def window():
    root = Tk()
    Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
