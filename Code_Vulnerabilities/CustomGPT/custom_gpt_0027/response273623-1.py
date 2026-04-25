
from tkinter import *

class Question:
    def __init__(self, master, question, options, correct_index):
        self.master = master
        self.question = question
        self.options = options
        self.correct_index = correct_index

        Label(self.master, text=self.question).grid()
        self.buttons = []

        for i, option in enumerate(self.options):
            button = Button(self.master, text=option, command=lambda index=i: self.check_answer(index))
            button.grid()
            self.buttons.append(button)

    def check_answer(self, index):
        for button in self.buttons:
            button.config(state=DISABLED)
        if index == self.correct_index:
            Label(self.master, text='Correct!').grid()
        else:
            Label(self.master, text='Incorrect!').grid()
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        self.master.destroy()  # Destroy the current window
        new_window = Toplevel()  # Create a new toplevel window
        if self.question == "What is 3 + 3?":
            Question(new_window, "What is 5 + 7?", ["11", "12"], 0)  # Example of the next question
        else:
            Label(new_window, text='Quiz Finished!').grid()

def start_quiz():
    root = Tk()
    Question(root, "What is 3 + 3?", ["5", "6"], 1)
    root.mainloop()

if __name__ == '__main__':
    start_quiz()
