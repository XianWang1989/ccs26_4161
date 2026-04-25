
from tkinter import *

class Question:
    def __init__(self, master, question_text, options, is_correct):
        self.master = master
        self.is_correct = is_correct
        Label(self.master, text=question_text).grid()

        for option in options:
            Button(self.master, text=option, command=lambda opt=option: self.check_answer(opt)).grid()

    def check_answer(self, selected_option):
        for widget in self.master.winfo_children():
            widget.destroy()  # Clear previous widgets

        if selected_option == self.is_correct:
            Label(self.master, text='Correct').grid()
        else:
            Label(self.master, text='Incorrect').grid()

        Button(self.master, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        # Destroy current window
        self.master.destroy()
        new_window = Toplevel()
        Question(new_window, 'What is 5 + 5?', ['10', '11', '12'], '10')

def start_quiz():
    root = Tk()
    Question(root, 'What is 3 + 3?', ['5', '6'], '6')
    root.mainloop()

if __name__ == '__main__':
    start_quiz()
