
import tkinter as tk

def create_window():
    window = tk.Tk()
    label = tk.Label(window, text="This text is larger!", font=("Arial", 20), fg="blue")
    label.pack()
    window.mainloop()

create_window()
