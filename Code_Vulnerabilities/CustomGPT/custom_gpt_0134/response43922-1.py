
from colorama import init, Fore
import tkinter as tk

# Initialize Colorama
init()

# Print blue text in the console
print(Fore.BLUE + "This is blue text in the console!")

# Create a simple tkinter window to show large text
root = tk.Tk()
root.title("Text Decoration Example")

# Create a label with larger text
label = tk.Label(root, text="This is larger text!", font=("Helvetica", 24), fg="blue")
label.pack(pady=20)

# Start the tkinter event loop
root.mainloop()
