
from tkinter import *

class Question:
    def __init__(self, master, question_text, correct_answer, next_question):
        self.master = master
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.next_question = next_question
        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text=self.question_text).grid()
        self.option_1 = Button(self.master, text='5', command=lambda: self.check_answer(5))
        self.option_1.grid()
        self.option_2 = Button(self.master, text=self.correct_answer, command=lambda: self.check_answer(int(self.correct_answer)))
        self.option_2.grid()

    def check_answer(self, answer):
        if answer == self.correct_answer:
            Label(self.master, text='Correct!').grid()
        else:
            Label(self.master, text='Incorrect!').grid()
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Button(self.master, text='Next Question', command=self.next_question_fn).grid()

    def next_question_fn(self):
        self.master.destroy()  # Destroy the current window
        new_window = Toplevel()  # Create a new Toplevel window
        if self.next_question:
            self.next_question(new_window)

def question_1(master):
    Question(master, 'What is 3 + 3?', 6, question_2)

def question_2(master):
    Question(master, 'What is 5 + 5?', 10, None)  # No next question

def window():
    root = Tk()
    question_1(root)
    root.mainloop()

if __name__ == '__main__':
    window()
