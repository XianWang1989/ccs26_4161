
from tkinter import *

class QuestionWindow:
    def __init__(self, master, question, options, correct_index):
        self.master = master
        self.question = question
        self.options = options
        self.correct_index = correct_index
        self.initialize()

    def initialize(self):
        Label(self.master, text=self.question).grid()
        for idx, option in enumerate(self.options):
            Button(self.master, text=option, command=lambda i=idx: self.check_answer(i)).grid()

    def check_answer(self, selected_index):
        for widget in self.master.winfo_children():
            widget.destroy()  # Clear the window

        if selected_index == self.correct_index:
            Label(self.master, text='Correct').grid()
        else:
            Label(self.master, text='Incorrect').grid()

        Button(self.master, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        new_window = Toplevel(self.master)
        # Create your next question here
        QuestionWindow(new_window, "What is 2 + 2?", ["3", "4"], 1)

def window():
    root = Tk()
    QuestionWindow(root, "What is 3 + 3?", ["5", "6"], 1)
    root.mainloop()

if __name__ == '__main__':
    window()
