
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = master  # Track the current question window
        self.show_question_1()

    def show_question_1(self):
        self.clear_window()  # Clear the window before showing a new question
        Label(self.question_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.question_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.question_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Correct').grid()
        Button(self.question_window, text='Next Question', command=self.show_question_2).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Incorrect').grid()
        Button(self.question_window, text='Next Question', command=self.show_question_2).grid()

    def show_question_2(self):
        self.clear_window()  # Clear the window before showing the next question
        Label(self.question_window, text='Question 2: What is 5 + 5?').grid()
        self.option_1 = Button(self.question_window, text='10', command=self.correct_answer)
        self.option_1.grid()
        self.option_2 = Button(self.question_window, text='11', command=self.incorrect_answer)
        self.option_2.grid()

    def correct_answer(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Correct').grid()
        Button(self.question_window, text='End Quiz', command=self.question_window.quit).grid()

    def incorrect_answer(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.question_window, text='Incorrect').grid()
        Button(self.question_window, text='End Quiz', command=self.question_window.quit).grid()

    def clear_window(self):
        for widget in self.question_window.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
