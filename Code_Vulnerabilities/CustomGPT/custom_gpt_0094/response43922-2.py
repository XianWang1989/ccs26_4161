
import tkinter as tk

root = tk.Tk()
root.title("Text Decoration Example")

label = tk.Label(root, text="This text is bigger!", font=("Helvetica", 32), fg="blue")
label.pack(pady=20)

root.mainloop()
