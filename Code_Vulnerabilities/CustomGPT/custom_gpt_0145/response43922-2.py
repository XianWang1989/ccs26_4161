
import tkinter as tk

root = tk.Tk()
root.title("Text Decoration Example")

# Customize the font size and color
label = tk.Label(root, text="This is bigger and blue text!", font=("Helvetica", 16), fg="blue")
label.pack(pady=20)

root.mainloop()
