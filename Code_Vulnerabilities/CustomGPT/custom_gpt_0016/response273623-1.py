
from tkinter import *

class QuestionWindow:
    def __init__(self, master, question, options, correct_index):
        self.master = master
        self.question_label = Label(self.master, text=question)
        self.question_label.grid()

        self.options = options
        self.correct_index = correct_index
        self.buttons = []

        for index, option in enumerate(self.options):
            button = Button(self.master, text=option, 
                            command=lambda idx=index: self.check_answer(idx))
            button.grid()
            self.buttons.append(button)

    def check_answer(self, selected_index):
        for button in self.buttons:
            button.config(state=DISABLED)

        if selected_index == self.correct_index:
            result_label = Label(self.master, text='Correct!')
        else:
            result_label = Label(self.master, text='Incorrect!')

        result_label.grid()

        next_button = Button(self.master, text='Next Question', command=self.next_question)
        next_button.grid()

    def next_question(self):
        self.master.destroy()  # Destroy the current window
        # Create a new window for the next question
        new_window = Toplevel()  
        QuestionWindow(new_window, "What is 5 + 5?", ['10', '11'], 0)

def start_quiz():
    root = Tk()
    QuestionWindow(root, "What is 3 + 3?", ['5', '6'], 1)
    root.mainloop()

if __name__ == '__main__':
    start_quiz()
