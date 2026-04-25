
import tkinter as tk

def create_window():
    root = tk.Tk()
    root.title("Text Decoration Example")

    label = tk.Label(root, text="This is a bigger blue text", fg="blue", font=("Helvetica", 16))
    label.pack(pady=20)

    root.mainloop()

create_window()
