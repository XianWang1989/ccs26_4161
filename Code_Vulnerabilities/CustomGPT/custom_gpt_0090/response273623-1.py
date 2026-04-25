
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = master
        self.render_question_1()

    def render_question_1(self):
        Label(self.current_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_window, text='Correct').grid()
        Button(self.current_window, text='Next Question', command=self.next_question).grid()

    def incorrect(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)
        Label(self.current_window, text='Incorrect').grid()
        Button(self.current_window, text='Next Question', command=self.next_question).grid()

    def next_question(self):
        self.current_window.destroy()  # Destroy previous window
        new_window = Toplevel(self.master)
        self.render_question_2(new_window)

    def render_question_2(self, master):
        Label(master, text='What is 4 + 4?').grid()
        Button(master, text='7', command=self.incorrect).grid()
        Button(master, text='8', command=self.correct).grid()

def main():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
