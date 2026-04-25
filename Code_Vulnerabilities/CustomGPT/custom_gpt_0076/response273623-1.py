
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None  # Track the current window
        self.show_question1()

    def show_question1(self):
        if self.current_window:
            self.current_window.destroy()  # Destroy the previous window
        self.current_window = Toplevel(self.master)
        Label(self.current_window, text='What is 3 + 3?').grid()
        Button(self.current_window, text='5', command=self.incorrect).grid()
        Button(self.current_window, text='6', command=self.correct).grid()

    def correct(self):
        self.show_feedback('Correct')

    def incorrect(self):
        self.show_feedback('Incorrect')

    def show_feedback(self, message):
        for widget in self.current_window.winfo_children():
            widget.destroy()  # Clear the window
        Label(self.current_window, text=message).grid()
        Button(self.current_window, text='Next Question', command=self.show_question2).grid()

    def show_question2(self):
        if self.current_window:
            self.current_window.destroy()  # Destroy the previous window
        self.current_window = Toplevel(self.master)
        Label(self.current_window, text='Question 2: What is 4 + 4?').grid()
        Button(self.current_window, text='7', command=self.incorrect).grid()
        Button(self.current_window, text='8', command=self.correct).grid()

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
