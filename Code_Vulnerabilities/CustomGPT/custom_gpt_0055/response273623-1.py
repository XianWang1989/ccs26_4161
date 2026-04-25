
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = master  # Keep track of the current window
        self.start_quiz()

    def start_quiz(self):
        self.show_question1()

    def show_question1(self):
        self.clear_window()
        Label(self.current_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.show_feedback("Correct")
        Button(self.current_window, text='Next Question', command=self.show_question2).grid()

    def incorrect(self):
        self.show_feedback("Incorrect")
        Button(self.current_window, text='Next Question', command=self.show_question2).grid()

    def show_feedback(self, message):
        Label(self.current_window, text=message).grid()
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

    def show_question2(self):
        self.clear_window()
        Label(self.current_window, text='Question 2').grid()

    def clear_window(self):
        for widget in self.current_window.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
