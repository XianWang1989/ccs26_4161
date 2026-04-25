
from tkinter import *

class QuizQuestion:
    def __init__(self, master, question_text, options, correct_index):
        self.master = master
        self.question_text = question_text
        self.options = options
        self.correct_index = correct_index

        Label(self.master, text=self.question_text).grid()
        self.buttons = []
        for i, option in enumerate(self.options):
            btn = Button(self.master, text=option, command=lambda i=i: self.check_answer(i))
            btn.grid()
            self.buttons.append(btn)

    def check_answer(self, selected_index):
        for btn in self.buttons:
            btn.config(state=DISABLED)
        if selected_index == self.correct_index:
            Label(self.master, text='Correct!').grid()
        else:
            Label(self.master, text='Incorrect!').grid()
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        self.master.destroy()  # Close the current window
        next_window()

def next_window():
    question_data = [
        ("What is 3 + 3?", ["5", "6"], 1),
        ("What is 2 + 2?", ["3", "4"], 1),
    ]

    if question_data:
        question = question_data.pop(0)
        new_window = Toplevel()
        QuizQuestion(new_window, *question)

def main_window():
    root = Tk()
    question_data = [
        ("What is 3 + 3?", ["5", "6"], 1),
    ]
    QuizQuestion(root, *question_data[0])
    root.mainloop()

if __name__ == '__main__':
    main_window()
