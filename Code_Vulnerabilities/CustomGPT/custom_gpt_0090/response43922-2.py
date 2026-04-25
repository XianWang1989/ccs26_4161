
import tkinter as tk

root = tk.Tk()

# Create a label with blue text
label = tk.Label(root, text="This is blue text.", fg="blue", font=("Helvetica", 16))
label.pack()

# Create another label with larger text
large_label = tk.Label(root, text="This is bigger text.", font=("Helvetica", 24))
large_label.pack()

root.mainloop()
