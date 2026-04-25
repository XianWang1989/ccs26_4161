
from tkinter import *

class Question:
    def __init__(self, master, question_text, correct_answer, next_question):
        self.master = master
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.next_question = next_question

        Label(self.master, text=self.question_text).grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text=correct_answer, command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.display_result('Correct')

    def incorrect(self):
        self.display_result('Incorrect')

    def display_result(self, result_text):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text=result_text).grid()
        Button(self.master, text='Next Question', command=self.next_question_callback).grid()

    def next_question_callback(self):
        self.master.destroy()  # Destroy current window
        next_question_window = Toplevel()  # Create new Toplevel window
        self.next_question(next_question_window)

def question1(master):
    Question(master, 'What is 3 + 3?', '6', question2)

def question2(master):
    Question(master, 'What is the capital of France?', 'Paris', lambda m: None)  # Placeholder for next question

def main_window():
    root = Tk()
    question1(root)
    root.mainloop()

if __name__ == '__main__':
    main_window()
