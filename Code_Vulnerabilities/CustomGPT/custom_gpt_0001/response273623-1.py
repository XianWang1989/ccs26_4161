
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None  # Initialize a variable to keep track of the current question window
        self.start_question_1()

    def start_question_1(self):
        # Destroy any previous question window if it exists
        if self.current_window is not None:
            self.current_window.destroy()

        # Create a new window for question 1
        self.current_window = Toplevel(self.master)
        q1(self.current_window)

class q1:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Correct').grid()
        Button(self.master, text='Next Question', command=self.nextq).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').grid()
        Button(self.master, text='Next Question', command=self.nextq).grid()

    def nextq(self):
        # Call the QuizApp to switch to the next question (question 2)
        app.start_question_2()

class q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 4 + 4?').grid()
        # Add similar options and logic as in q1

def window():
    root = Tk()
    global app  # Ensure app is accessible globally for switching questions
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
