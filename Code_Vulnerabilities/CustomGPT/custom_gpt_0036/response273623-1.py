
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.start_question()

    def start_question(self):
        self.question1 = Question1(self.master)

class Question1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        Label(self.frame, text='What is 3 + 3?').grid(row=0, column=0)

        self.option_1 = Button(self.frame, text='5', command=self.incorrect)
        self.option_1.grid(row=1, column=0)

        self.option_2 = Button(self.frame, text='6', command=self.correct)
        self.option_2.grid(row=1, column=1)

    def correct(self):
        self.update_buttons()
        Label(self.frame, text='Correct').grid(row=2, column=0)
        Button(self.frame, text='Next Question', command=self.next_question).grid(row=3, column=0)

    def incorrect(self):
        self.update_buttons()
        Label(self.frame, text='Incorrect').grid(row=2, column=0)
        Button(self.frame, text='Next Question', command=self.next_question).grid(row=3, column=0)

    def update_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

    def next_question(self):
        self.frame.destroy()  # Destroy the current frame
        Question2(self.master)  # Create the next question

class Question2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        Label(self.frame, text='What is 5 + 5?').grid(row=0, column=0)

        self.option_1 = Button(self.frame, text='10', command=self.correct)
        self.option_1.grid(row=1, column=0)

        self.option_2 = Button(self.frame, text='11', command=self.incorrect)
        self.option_2.grid(row=1, column=1)

    def correct(self):
        self.update_buttons()
        Label(self.frame, text='Correct').grid(row=2, column=0)
        Button(self.frame, text='Finish', command=self.finish).grid(row=3, column=0)

    def incorrect(self):
        self.update_buttons()
        Label(self.frame, text='Incorrect').grid(row=2, column=0)
        Button(self.frame, text='Finish', command=self.finish).grid(row=3, column=0)

    def update_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

    def finish(self):
        self.frame.destroy()  # Optionally destroy frame once finished
        Label(self.master, text='Quiz Finished!').pack()

def window():
    root = Tk()
    QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
