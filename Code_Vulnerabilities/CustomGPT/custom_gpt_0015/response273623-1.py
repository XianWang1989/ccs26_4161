
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.show_question_1()

    def show_question_1(self):
        self.current_window = Frame(self.master)
        self.current_window.pack()

        Label(self.current_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.disable_options()
        Label(self.current_window, text='Correct').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def incorrect(self):
        self.disable_options()
        Label(self.current_window, text='Incorrect').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def disable_options(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

    def show_question_2(self):
        self.current_window.destroy()  # Destroy the current window
        self.current_window = Frame(self.master)
        self.current_window.pack()

        Label(self.current_window, text='What is 4 + 4?').grid()
        self.option_1 = Button(self.current_window, text='8', command=self.correct2)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='7', command=self.incorrect2)
        self.option_2.grid()

    def correct2(self):
        self.disable_options()
        Label(self.current_window, text='Correct').grid()

    def incorrect2(self):
        self.disable_options()
        Label(self.current_window, text='Incorrect').grid()

def main():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
