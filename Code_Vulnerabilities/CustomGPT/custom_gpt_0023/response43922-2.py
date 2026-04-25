
import tkinter as tk

root = tk.Tk()
root.title("Text Decoration Example")

# Create a label with larger text
label = tk.Label(root, text="This is bigger text!", font=("Arial", 24), fg="blue")
label.pack(pady=20)

# Start the GUI loop
root.mainloop()
