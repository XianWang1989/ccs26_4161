
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.question1()

    def question1(self):
        self.clear_window()
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.display_feedback('Correct')
        Button(self.master, text='Next Question', command=self.question2).grid()

    def incorrect(self):
        self.display_feedback('Incorrect')
        Button(self.master, text='Next Question', command=self.question2).grid()

    def display_feedback(self, message):
        Label(self.master, text=message).grid()

    def question2(self):
        self.clear_window()
        Label(self.master, text='What is 5 + 5?').grid()
        self.option_1 = Button(self.master, text='10', command=self.correct_q2)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='11', command=self.incorrect_q2)
        self.option_2.grid()

    def correct_q2(self):
        self.display_feedback('Correct')
        Button(self.master, text='Finish', command=self.master.quit).grid()

    def incorrect_q2(self):
        self.display_feedback('Incorrect')
        Button(self.master, text='Finish', command=self.master.quit).grid()

    def clear_window(self):
        # Clearing previous widgets in the window
        for widget in self.master.winfo_children():
            widget.destroy()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
