
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.current_question = None
        self.start_question1()

    def start_question1(self):
        self.current_question = q1(self.master, self)

    def start_question2(self):
        self.current_question.destroy()  # Destroy previous question window
        self.current_question = q2(self.master, self)

class q1:
    def __init__(self, master, quiz):
        self.master = master
        self.quiz = quiz
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.display_result('Correct')

    def incorrect(self):
        self.display_result('Incorrect')

    def display_result(self, message):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text=message).grid()
        Button(self.master, text='Next Question', command=self.quiz.start_question2).grid()

    def destroy(self):
        for widget in self.master.winfo_children():
            widget.destroy()

class q2:
    def __init__(self, master, quiz):
        self.master = master
        self.quiz = quiz
        Label(self.master, text='What is 5 + 5?').grid()
        Button(self.master, text='10', command=self.correct).grid()
        Button(self.master, text='11', command=self.incorrect).grid()

    def correct(self):
        self.display_result('Correct')

    def incorrect(self):
        self.display_result('Incorrect')

    def display_result(self, message):
        Label(self.master, text=message).grid()
        Button(self.master, text='Finish', command=self.quiz.destroy_quiz).grid()

    def destroy(self):
        for widget in self.master.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    app = Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
