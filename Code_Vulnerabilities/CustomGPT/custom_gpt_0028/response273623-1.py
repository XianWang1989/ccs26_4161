
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.create_question_1()

    def create_question_1(self):
        self.clear_window()
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.disable_options()
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=self.create_question_2).grid()

    def incorrect(self):
        self.disable_options()
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.create_question_2).grid()

    def create_question_2(self):
        self.clear_window()
        Label(self.master, text='What is 4 + 4?').grid()
        self.option_1 = Button(self.master, text='8', command=self.correct)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='9', command=self.incorrect)
        self.option_2.grid()

    def disable_options(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
