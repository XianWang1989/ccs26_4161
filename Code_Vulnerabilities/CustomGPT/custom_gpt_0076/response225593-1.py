
import tkinter as tk
from tkinter import filedialog

def save_file_name():
    file_name = filedialog.askopenfilename()
    if file_name:  # Check if a file was selected
        with open("output.txt", "w") as conf:
            conf.write(f"receptor='{file_name}'\n")
            print(f"File name '{file_name}' saved to output.txt")

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Dialog Example")
mGui.geometry("500x200")

# Create the Browse button
browse_button = tk.Button(mGui, text='Browse', command=save_file_name)
browse_button.place(x=200, y=50)

mGui.mainloop()
