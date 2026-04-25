
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = master
        self.question1()

    def question1(self):
        self.clear_window()
        Label(self.current_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self.show_feedback('Correct')
        Button(self.current_window, text='Next Question', command=self.question2).grid()

    def incorrect(self):
        self.show_feedback('Incorrect')
        Button(self.current_window, text='Next Question', command=self.question2).grid()

    def show_feedback(self, feedback):
        Label(self.current_window, text=feedback).grid()

    def question2(self):
        self.clear_window()
        Label(self.current_window, text='What is 5 + 5?').grid()
        self.option_1 = Button(self.current_window, text='10', command=self.correct)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='11', command=self.incorrect)
        self.option_2.grid()

    def clear_window(self):
        for widget in self.current_window.winfo_children():
            widget.destroy()

def main():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
