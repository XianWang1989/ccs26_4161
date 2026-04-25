
from tkinter import *

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.show_question_1()

    def show_question_1(self):
        # Create the first question window
        self.current_window = Toplevel(self.master)
        Label(self.current_window, text='What is 3 + 3?').grid()
        self.option_1 = Button(self.current_window, text='5', command=self.incorrect)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='6', command=self.correct)
        self.option_2.grid()

    def correct(self):
        self._disable_buttons()
        Label(self.current_window, text='Correct!').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def incorrect(self):
        self._disable_buttons()
        Label(self.current_window, text='Incorrect!').grid()
        Button(self.current_window, text='Next Question', command=self.show_question_2).grid()

    def show_question_2(self):
        self.current_window.destroy()  # Destroy the current question window
        self.show_question_2_window()

    def show_question_2_window(self):
        # Create the second question window
        self.current_window = Toplevel(self.master)
        Label(self.current_window, text='What is 5 + 5?').grid()
        self.option_1 = Button(self.current_window, text='10', command=self.correct_2)
        self.option_1.grid()
        self.option_2 = Button(self.current_window, text='11', command=self.incorrect_2)
        self.option_2.grid()

    def correct_2(self):
        self._disable_buttons()
        Label(self.current_window, text='Correct!').grid()

    def incorrect_2(self):
        self._disable_buttons()
        Label(self.current_window, text='Incorrect!').grid()

    def _disable_buttons(self):
        self.option_1.config(state=DISABLED)
        self.option_2.config(state=DISABLED)

def main():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
