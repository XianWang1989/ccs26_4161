
from tkinter import *

class QuizWindow:
    def __init__(self, master):
        self.master = master
        self.current_question = None
        self.show_question1()

    def show_question1(self):
        self.destroy_current()
        self.current_question = Question1(self.master, self)

    def show_question2(self):
        self.destroy_current()
        self.current_question = Question2(self.master, self)

    def destroy_current(self):
        if self.current_question:
            self.current_question.destroy()

class Question1:
    def __init__(self, master, parent):
        self.master = master
        self.parent = parent
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.show_feedback('Correct')
        Button(self.master, text='Next Question', command=self.parent.show_question2).grid()

    def incorrect(self):
        self.show_feedback('Incorrect')
        Button(self.master, text='Next Question', command=self.parent.show_question2).grid()

    def show_feedback(self, message):
        Label(self.master, text=message).grid()

    def destroy(self):
        for widget in self.master.grid_slaves():
            widget.destroy()

class Question2:
    def __init__(self, master, parent):
        self.master = master
        self.parent = parent
        Label(self.master, text='What is 2 + 2?').grid()
        # Add options and buttons similar to Question1

    def destroy(self):
        for widget in self.master.grid_slaves():
            widget.destroy()

def window():
    root = Tk()
    QuizWindow(root)
    root.mainloop()

if __name__ == '__main__':
    window()
