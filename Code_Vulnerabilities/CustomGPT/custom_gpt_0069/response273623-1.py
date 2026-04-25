
from tkinter import *

class Q1:
    def __init__(self, master):
        self.master = master
        self.question_label = Label(self.master, text='What is 3 + 3?')
        self.question_label.pack()

        self.option_1 = Button(self.master, text='5', command=self.incorrect)
        self.option_1.pack()
        self.option_2 = Button(self.master, text='6', command=self.correct)
        self.option_2.pack()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Correct').pack()
        Button(self.master, text='Next Question', command=self.next_q).pack()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.master, text='Incorrect').pack()
        Button(self.master, text='Next Question', command=self.next_q).pack()

    def next_q(self):
        self.master.destroy()  # Destroy the current window
        new_window = Toplevel()  # Create a new Toplevel window
        Q2(new_window)  # Pass the new window to the next question class

class Q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='Question 2').pack()

def window():
    root = Tk()
    Q1(root)
    root.mainloop()

if __name__ == '__main__':
    window()
