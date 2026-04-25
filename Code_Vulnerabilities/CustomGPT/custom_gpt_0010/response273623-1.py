
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_question = None
        self.start_question1()

    def start_question1(self):
        self.current_question = Question1(self.master, self)

    def go_to_next_question(self):
        if self.current_question:
            self.current_question.master.destroy()  # Destroy the current question window
        self.start_question2()

    def start_question2(self):
        self.current_question = Question2(self.master, self)

class Question1:
    def __init__(self, master, app):
        self.master = Toplevel(master)
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()
        self.app = app

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=self.app.go_to_next_question).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.app.go_to_next_question).grid()

class Question2:
    def __init__(self, master, app):
        self.master = Toplevel(master)
        Label(self.master, text='Question 2').grid()
        # Add more options or logic as needed

def main():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
