
from tkinter import *

class q1:
    def __init__(self, master):
        self.master = master
        self.label = Label(self.master, text='What is 3 + 3?')
        self.label.grid()
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
        self.master.destroy()  # Destroy the current window
        new_window = Tk()      # Create a new root window for the next question
        q2(new_window)        # Initialize q2 with the new window
        new_window.mainloop()  # Start the event loop for the new window

class q2:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='What is 4 + 4?').grid()
        Button(self.master, text='8', command=lambda: self.correct(master)).grid()
        Button(self.master, text='9', command=self.incorrect).grid()

    def correct(self, master):
        Label(master, text='Correct').grid()
        Button(master, text='Next Question', command=lambda: self.nextq(master)).grid()

    def incorrect(self):
        Label(self.master, text='Incorrect').grid()

    def nextq(self, master):
        # Logic for the next question can go here
        master.destroy()  # Optionally destroy before the next question
        new_window = Tk()
        # Initialize the next question class here, e.g., q3(new_window)
        # q3(new_window)
        new_window.mainloop()

def window():
    root = Tk()
    q1(root)
    root.mainloop()

if __name__ == '__main__':
    window()
