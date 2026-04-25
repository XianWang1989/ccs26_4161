
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.window = master
        self.current_question = 1  # Track the current question
        self.show_question_1()  # Start with the first question

    def show_question_1(self):
        self.clear_window()  # Clear previous widgets
        Label(self.window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.window, text='6', command=self.correct)
        self.option_2.grid()

    def show_question_2(self):
        self.clear_window()  # Clear previous widgets
        Label(self.window, text='What is 5 + 5?').grid()
        self.option_1 = Button(self.window, text='10', command=self.correct)
        self.option_1.grid()
        self.option_2 = Button(self.window, text='12', command=self.incorrect)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.window, text='Correct').grid()
        Button(self.window, text='Next Question', command=self.next_question).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.window, text='Incorrect').grid()
        Button(self.window, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        if self.current_question == 1:
            self.current_question = 2
            self.show_question_2()
        else:
            Label(self.window, text='Quiz Completed!').grid()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    app = Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
