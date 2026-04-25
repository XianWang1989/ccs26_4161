
import tkinter as tk

# Create a window
root = tk.Tk()

# Create a label with blue text and larger font
label = tk.Label(root, text="This text is blue and bigger!", fg="blue", font=("Helvetica", 16))
label.pack()

# Run the application
root.mainloop()
