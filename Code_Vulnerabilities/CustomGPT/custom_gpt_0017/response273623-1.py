
from tkinter import *

class Question:
    def __init__(self, master, question_text, options, correct_index, next_question=None):
        self.master = master
        self.question_text = question_text
        self.options = options
        self.correct_index = correct_index
        self.next_question = next_question
        self.setup_ui()

    def setup_ui(self):
        Label(self.master, text=self.question_text).grid()
        for idx, (text, command) in enumerate(self.options):
            Button(self.master, text=text, command=lambda index=idx: self.check_answer(index)).grid()

    def check_answer(self, index):
        for button in self.master.grid_slaves():
            button.config(state=DISABLED)

        if index == self.correct_index:
            Label(self.master, text='Correct').grid()
        else:
            Label(self.master, text='Incorrect').grid()

        Button(self.master, text='Next Question', command=self.nextq).grid()

    def nextq(self):
        self.master.destroy()  # Destroy the current window
        new_window = Toplevel()
        self.next_question(new_window)

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.start_quiz()

    def start_quiz(self):
        self.q1 = Question(self.master, 
                           'What is 3 + 3?', 
                           [('5', lambda: None), ('6', lambda: None)], 
                           correct_index=1, 
                           next_question=self.q2)

    def q2(self, master):
        Question(master, 
                 'Question 2: What is 5 + 2?', 
                 [('6', lambda: None), ('7', lambda: None)], 
                 correct_index=1)

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
