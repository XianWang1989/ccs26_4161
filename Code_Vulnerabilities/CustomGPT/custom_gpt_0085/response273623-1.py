
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = master
        self.question1()

    def question1(self):
        self.clear_window()
        Label(self.current_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.disable_buttons()
        Label(self.current_window, text='Correct!').grid()
        Button(self.current_window, text='Next Question', command=self.question2).grid()

    def incorrect(self):
        self.disable_buttons()
        Label(self.current_window, text='Incorrect!').grid()
        Button(self.current_window, text='Next Question', command=self.question2).grid()

    def question2(self):
        self.clear_window()
        Label(self.current_window, text='What is 2 + 2?').grid()
        self.option_1 = Button(self.current_window, text='3', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='4', command=self.correct)
        self.option_2.grid()

    def disable_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

    def clear_window(self):
        for widget in self.current_window.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
