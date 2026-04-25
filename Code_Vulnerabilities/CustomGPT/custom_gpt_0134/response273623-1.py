
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_question = None
        self.show_question_1()

    def show_question_1(self):
        # Destroy any previous question window
        if self.current_question:
            self.current_question.destroy()
        self.current_question = Toplevel(self.master)
        Label(self.current_question, text='What is 3 + 3?').grid()

        Button(self.current_question, text='5', command=self.incorrect).grid()
        Button(self.current_question, text='6', command=self.correct).grid()

    def correct(self):
        self.show_feedback("Correct")

    def incorrect(self):
        self.show_feedback("Incorrect")

    def show_feedback(self, message):
        for widget in self.current_question.winfo_children():
            widget.destroy()
        Label(self.current_question, text=message).grid()
        Button(self.current_question, text='Next Question', command=self.show_question_2).grid()

    def show_question_2(self):
        self.show_question_1()  # For demonstration, you could create another method for a real question.

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
