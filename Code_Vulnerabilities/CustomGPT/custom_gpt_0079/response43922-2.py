
import tkinter as tk

# Create a window
root = tk.Tk()
root.title("Text Decoration Example")

# Create a label with blue text and font size 24
label = tk.Label(root, text="This text is blue and larger!", fg="blue", font=("Helvetica", 24))
label.pack(pady=20)

# Run the application
root.mainloop()
