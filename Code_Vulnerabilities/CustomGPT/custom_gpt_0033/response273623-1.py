
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
            button = Button(self.master, text=option, command=lambda index=i: self.check_answer(index))
            button.grid()

    def check_answer(self, index):
        self.disable_buttons()
        if index == self.correct_index:
            Label(self.master, text='Correct').grid()
        else:
            Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.next_question).grid()

    def disable_buttons(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, Button):
                widget.config(state=DISABLED)

    def next_question(self):
        self.master.destroy()  # Close the current window
        new_window = Toplevel()  # Create new window
        self.load_next_question(new_window)

    def load_next_question(self, master):
        # Define next question and options
        if isinstance(self, Question1):
            Question(master, 'What is 2 + 2?', ['3', '4'], 1)
        else:
            Label(master, text='Quiz over!').grid()

class Question1(Question):
    def __init__(self, master):
        super().__init__(master, 'What is 3 + 3?', ['5', '6'], 1)

def window():
    root = Tk()
    Question1(root)
    root.mainloop()

if __name__ == '__main__':
    window()
