
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.show_question_1()

    def show_question_1(self):
        self.current_window = Frame(self.master)
        self.current_window.pack()
        Label(self.current_window, text='What is 3 + 3?').grid()
        Button(self.current_window, text='5', command=self.incorrect).grid()
        Button(self.current_window, text='6', command=self.correct).grid()

    def correct(self):
        self.disable_buttons()
        Label(self.current_window, text='Correct').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def incorrect(self):
        self.disable_buttons()
        Label(self.current_window, text='Incorrect').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def disable_buttons(self):
        for widget in self.current_window.winfo_children():
            if isinstance(widget, Button):
                widget.config(state=DISABLED)

    def show_question_2(self):
        self.current_window.destroy()  # Destroy the current window
        self.current_window = Frame(self.master)
        self.current_window.pack()
        Label(self.current_window, text='Question 2').grid()
        Button(self.current_window, text='Next Question', command=self.end_quiz).grid()

    def end_quiz(self):
        self.current_window.destroy()
        Label(self.master, text='Quiz Completed!').pack()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
