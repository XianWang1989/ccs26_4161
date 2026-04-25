
from tkinter import *

class Quiz:
    def __init__(self, master):
        self.master = master
        self.current_window = None
        self.question_1()

    def question_1(self):
        self.current_window = Toplevel(self.master)
        self.current_window.title("Question 1")
        Label(self.current_window, text='What is 3 + 3?').grid()
        option_1 = Button(self.current_window, text='5', command=lambda: self.incorrect(self.current_window))
        option_1.grid()
        option_2 = Button(self.current_window, text='6', command=lambda: self.correct(self.current_window))
        option_2.grid()

    def correct(self, window):
        self.show_result(window, 'Correct')
        self.next_question(window)

    def incorrect(self, window):
        self.show_result(window, 'Incorrect')
        self.next_question(window)

    def show_result(self, window, result_text):
        Label(window, text=result_text).grid()
        for widget in window.winfo_children():  # Disable all buttons
            if isinstance(widget, Button):
                widget.config(state=DISABLED)

    def next_question(self, window):
        window.destroy()  # Destroy the current window
        self.question_2()  # Create the next question window

    def question_2(self):
        self.current_window = Toplevel(self.master)
        self.current_window.title("Question 2")
        Label(self.current_window, text='What is 5 + 5?').grid()
        option_1 = Button(self.current_window, text='10', command=lambda: self.correct(self.current_window))
        option_1.grid()
        option_2 = Button(self.current_window, text='11', command=lambda: self.incorrect(self.current_window))
        option_2.grid()

def window():
    root = Tk()
    Quiz(root)
    root.mainloop()

if __name__ == '__main__':
    window()
