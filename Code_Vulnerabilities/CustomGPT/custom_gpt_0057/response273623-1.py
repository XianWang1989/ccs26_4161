
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
        for i, option in enumerate(self.options):
            Button(self.master, text=option, command=lambda index=i: self.check_answer(index)).grid()

    def check_answer(self, selected_index):
        for widget in self.master.winfo_children():
            widget.destroy()
        if selected_index == self.correct_index:
            Label(self.master, text='Correct').grid()
        else:
            Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        self.master.destroy()
        if self.question_text == 'Question 1':
            q2(Toplevel(root))
        else:
            Label(root, text='Quiz Finished').grid()

class q1(Question):
    def __init__(self, master):
        super().__init__(master, 'What is 3 + 3?', ['5', '6'], 1)

class q2(Question):
    def __init__(self, master):
        super().__init__(master, 'What is 5 + 5?', ['10', '11'], 0)

def window():
    global root
    root = Tk()
    q1(root)
    root.mainloop()

if __name__ == '__main__':
    window()
