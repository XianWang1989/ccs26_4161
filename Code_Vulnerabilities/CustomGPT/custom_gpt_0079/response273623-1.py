
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
        self.show_feedback('Correct')
        Button(self.master, text='Next Question', command=self.create_question_2).grid()

    def incorrect(self):
        self.show_feedback('Incorrect')
        Button(self.master, text='Next Question', command=self.create_question_2).grid()

    def show_feedback(self, message):
        Label(self.master, text=message).grid()

    def create_question_2(self):
        self.clear_window()
        Label(self.master, text='Question 2: What is 2 + 2?').grid()
        self.option_1 = Button(self.master, text='3', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='4', command=self.correct_q2)
        self.option_2.grid()

    def correct_q2(self):
        self.show_feedback('Correct on Question 2')
        Button(self.master, text='Finish', command=self.master.destroy).grid()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
