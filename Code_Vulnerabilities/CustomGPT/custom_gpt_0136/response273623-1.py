
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_question = None
        self.show_question_1()

    def show_question_1(self):
        self.current_question = Frame(self.master)
        self.current_question.pack()

        Label(self.current_question, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_question, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_question, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.process_answer("Correct")

    def incorrect(self):
        self.process_answer("Incorrect")

    def process_answer(self, message):
        for widget in self.current_question.winfo_children():
            widget.destroy()

        Label(self.current_question, text=message).grid()
        Button(self.current_question, text='Next Question', command=self.show_question_2).grid()

    def show_question_2(self):
        for widget in self.current_question.winfo_children():
            widget.destroy()

        Label(self.current_question, text='What is 4 + 4?').grid()
        self.option_3 = Button(self.current_question, text='7', command=self.incorrect)
        self.option_3.grid()
        self.option_4 = Button(self.current_question, text='8', command=self.correct)
        self.option_4.grid()

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
