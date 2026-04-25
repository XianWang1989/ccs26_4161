
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the title
root.title("Text Decoration Example")

# Create a label with larger, blue text
label = tk.Label(root, text="This text is blue and bigger!", font=("Helvetica", 20), fg="blue")
label.pack(pady=20)

# Run the application
root.mainloop()
