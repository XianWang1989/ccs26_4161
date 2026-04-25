
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.current_window = master
        self.show_question_1()

    def show_question_1(self):
        self.clear_window()
        Label(self.current_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_window, text='Correct').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_window, text='Incorrect').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def show_question_2(self):
        self.clear_window()
        Label(self.current_window, text='What is 5 + 5?').grid()
        self.option_1 = Button(self.current_window, text='10', command=self.correct)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='11', command=self.incorrect)
        self.option_2.grid()

    def clear_window(self):
        for widget in self.current_window.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
