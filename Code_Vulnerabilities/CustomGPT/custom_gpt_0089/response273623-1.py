
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_question = None
        self.create_question1()

    def create_question1(self):
        self.current_question = Question1(self.master, self)

    def create_question2(self):
        self.current_question.destroy()  # Destroy the previous question
        self.current_question = Question2(self.master, self)

class Question1:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.display_result("Correct")

    def incorrect(self):
        self.display_result("Incorrect")

    def display_result(self, message):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text=message).grid()
        Button(self.master, text='Next Question', command=self.app.create_question2).grid()

    def destroy(self):
        for widget in self.master.winfo_children():
            widget.destroy()

class Question2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 5 + 5?').grid()
        self.option_1 = Button(self.master, text='10', command=self.correct)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='11', command=self.incorrect)
        self.option_2.grid()

    def correct(self):
        self.display_result("Correct")

    def incorrect(self):
        self.display_result("Incorrect")

    def display_result(self, message):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text=message).grid()
        Button(self.master, text='Finish', command=self.master.quit).grid()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
