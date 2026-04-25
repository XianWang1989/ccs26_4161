
from tkinter import *

class Question:
    def __init__(self, master, question_text, options, correct_index):
        self.master = master
        self.question_text = question_text
        self.options = options
        self.correct_index = correct_index

        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text=self.question_text).grid()
        self.buttons = []
        for index, option in enumerate(self.options):
            button = Button(self.master, text=option, command=lambda idx=index: self.check_answer(idx))
            self.buttons.append(button)
            button.grid()

    def check_answer(self, selected_index):
        for button in self.buttons:
            button.config(state=DISABLED)
        if selected_index == self.correct_index:
            Label(self.master, text='Correct').grid()
        else:
            Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        self.master.destroy()  # Destroy current window
        new_window = Toplevel()
        if self.question_text == 'What is 3 + 3?':
            Question(new_window, 'Question 2', ['Option A', 'Option B'], 0)
        else:
            Label(new_window, text='End of Quiz').grid()

def window():
    root = Tk()
    Question(root, 'What is 3 + 3?', ['5', '6'], 1)  # 1 is the correct index for '6'
    root.mainloop()

if __name__ == '__main__':
    window()
