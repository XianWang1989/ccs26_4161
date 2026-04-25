
import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write(f'receptor="{filename}"\n')
        print(f'Selected file: {filename}')

# Set up the main GUI window
mGui = tk.Tk()
mGui.title("File Selector")

browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
