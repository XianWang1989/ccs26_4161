
import tkinter as tk

root = tk.Tk()
root.title("Text Decoration Example")

label = tk.Label(root, text="This text is big and blue!", font=("Arial", 24), fg="blue")
label.pack(pady=20)

root.mainloop()
