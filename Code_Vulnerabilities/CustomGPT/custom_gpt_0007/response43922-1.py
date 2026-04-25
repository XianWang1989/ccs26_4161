
import tkinter as tk

root = tk.Tk()
root.title("Text Decoration Example")

label = tk.Label(root, text="Hello, World!", fg="blue", font=("Helvetica", 16))
label.pack(pady=20)

root.mainloop()
