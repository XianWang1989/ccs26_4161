
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = master  # Start with the main window
        self.start_quiz()  # Start the quiz in the main window

    def start_quiz(self):
        self.open_question_1()

    def open_question_1(self):
        self.current_window.withdraw()  # Hide the previous window
        self.current_window = Toplevel(self.master)  # Create a new Toplevel window
        q1(self.current_window, self)

class q1:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.disable_buttons()
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=self.nextq).grid()

    def incorrect(self):
        self.disable_buttons()
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.nextq).grid()

    def disable_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

    def nextq(self):
        self.master.destroy()  # Close the current question window
        self.app.open_question_2()  # Open the next question

class q2:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        Label(self.master, text='What is 4 + 4?').grid()
        self.option_1 = Button(self.master, text='8', command=self.correct)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='7', command=self.incorrect)
        self.option_2.grid()

    def correct(self):
        self.disable_buttons()
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Finish', command=self.master.destroy).grid()

    def incorrect(self):
        self.disable_buttons()
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Finish', command=self.master.destroy).grid()

    def disable_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
