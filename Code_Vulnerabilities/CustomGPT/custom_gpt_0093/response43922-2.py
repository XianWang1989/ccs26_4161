
import tkinter as tk

root = tk.Tk()
root.title("Text Decoration Example")

# Create a label with larger and blue text
label = tk.Label(root, text="This text is blue and larger!", font=("Arial", 20), fg="blue")
label.pack(pady=20)

root.mainloop()
