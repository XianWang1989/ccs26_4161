
import Tkinter as tk  # For Python 2.x
from Tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()  # Open file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write(f'receptor="{filename}"\n')  # Write file path to a text file
        print(f'Selected file: {filename}')  # Optional: print to console

# Set up the main application window
mGui = tk.Tk()
mGui.title("File Selector")
mGui.geometry("500x200")

# Add browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=200, y=50)

mGui.mainloop()
