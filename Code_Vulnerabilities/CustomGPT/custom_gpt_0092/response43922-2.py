
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Text Decoration Example")

# Create a label with styled text
label = tk.Label(root, text="Hello, world!", fg="blue", font=("Helvetica", 24))
label.pack()

# Start the GUI event loop
root.mainloop()
