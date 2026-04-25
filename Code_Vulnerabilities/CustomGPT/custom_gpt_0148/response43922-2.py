
import tkinter as tk

root = tk.Tk()
root.title("Text Decoration Example")

label = tk.Label(root, text="This text is blue and bigger!", font=("Helvetica", 16), fg="blue")
label.pack(pady=20)

root.mainloop()
