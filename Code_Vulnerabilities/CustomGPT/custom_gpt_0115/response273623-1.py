
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.create_q1()

    def create_q1(self):
        self.q1_frame = Frame(self.master)
        self.q1_frame.pack()

        Label(self.q1_frame, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.q1_frame, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.q1_frame, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.q1_frame, text='Correct').grid()
        Button(self.q1_frame, text='Next Question', command=self.next_question).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.q1_frame, text='Incorrect').grid()
        Button(self.q1_frame, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        self.q1_frame.destroy()  # Destroy the current frame
        self.create_q2()  # Create the next question window

    def create_q2(self):
        self.q2_frame = Frame(self.master)
        self.q2_frame.pack()

        Label(self.q2_frame, text='What is 4 + 4?').grid()
        Button(self.q2_frame, text='8', command=self.correct_q2).grid()
        Button(self.q2_frame, text='9', command=self.incorrect_q2).grid()

    def correct_q2(self):
        Label(self.q2_frame, text='Correct').grid()

    def incorrect_q2(self):
        Label(self.q2_frame, text='Incorrect').grid()

def window():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
