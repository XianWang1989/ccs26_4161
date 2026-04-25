
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Text Decoration Example")

# Create a label with larger font and blue color
label = tk.Label(root, text="Hello, this is blue and bigger!", font=("Helvetica", 16), fg="blue")
label.pack()

# Run the application
root.mainloop()
