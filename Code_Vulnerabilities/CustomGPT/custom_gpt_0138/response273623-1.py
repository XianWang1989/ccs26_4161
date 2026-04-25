
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.show_q1()

    def show_q1(self):
        if self.current_window:
            self.current_window.destroy()
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
        app.show_q2()

class q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='Question 2').grid()

def window():
    root = Tk()
    global app
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    window()
