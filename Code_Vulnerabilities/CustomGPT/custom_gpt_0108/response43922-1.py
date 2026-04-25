
import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Text Decoration Example")

    label = tk.Label(window, text="Hello, World!", fg="blue", font=("Helvetica", 16))
    label.pack(pady=20)

    window.mainloop()

create_window()
