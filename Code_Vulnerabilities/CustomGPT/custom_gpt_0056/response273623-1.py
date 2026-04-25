
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question_window = None
        self.show_question_1()

    def show_question_1(self):
        self._create_question_window('What is 3 + 3?', self.correct_q1, self.incorrect_q1)

    def correct_q1(self):
        self._update_question_window('Correct! Press Next for Question 2.', self.show_question_2)

    def incorrect_q1(self):
        self._update_question_window('Incorrect! Press Next for Question 2.', self.show_question_2)

    def show_question_2(self):
        self._create_question_window('What is 2 + 2?', self.correct_q2, self.incorrect_q2)

    def correct_q2(self):
        self._update_question_window('Correct!', None)

    def incorrect_q2(self):
        self._update_question_window('Incorrect!', None)

    def _create_question_window(self, question, correct_command, incorrect_command):
        if self.question_window is not None:
            self.question_window.destroy()
        self.question_window = Toplevel(self.master)
        Label(self.question_window, text=question).grid()
        Button(self.question_window, text='5', command=incorrect_command).grid()
        Button(self.question_window, text='6', command=correct_command).grid()

    def _update_question_window(self, message, next_question):
        for widget in self.question_window.winfo_children():
            widget.destroy()
        Label(self.question_window, text=message).grid()
        if next_question:
            Button(self.question_window, text='Next Question', command=next_question).grid()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
