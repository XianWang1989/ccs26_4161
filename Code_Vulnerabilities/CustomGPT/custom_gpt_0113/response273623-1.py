
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.question1()

    def question1(self):
        self.clear_window()
        Label(self.master, text='What is 3 + 3?').grid()

        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.show_feedback('Correct')
        Button(self.master, text='Next Question', command=self.question2).grid()

    def incorrect(self):
        self.show_feedback('Incorrect')
        Button(self.master, text='Next Question', command=self.question2).grid()

    def show_feedback(self, feedback):
        Label(self.master, text=feedback).grid()
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

    def question2(self):
        self.clear_window()
        Label(self.master, text='What is the capital of France?').grid()
        self.option_3 = Button(self.master, text='Paris', command=self.correct_q2)
        self.option_3.grid()
        self.option_4 = Button(self.master, text='London', command=self.incorrect_q2)
        self.option_4.grid()

    def correct_q2(self):
        self.show_feedback('Correct')

    def incorrect_q2(self):
        self.show_feedback('Incorrect')

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
