
import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Text Decoration Example")

    # Create a label with blue text and a larger font
    label = tk.Label(window, text="Hello, World!", fg="blue", font=("Helvetica", 24))
    label.pack(pady=20)

    window.mainloop()

create_window()
