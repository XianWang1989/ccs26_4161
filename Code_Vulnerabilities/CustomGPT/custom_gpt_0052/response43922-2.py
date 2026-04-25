
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Styled Text Example")

# Create a label with styled text
label = tk.Label(root, text="This text is blue and larger!", fg="blue", font=("Helvetica", 16))
label.pack()

# Run the application
root.mainloop()
