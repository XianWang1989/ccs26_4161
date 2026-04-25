
import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:
            conf.write(f'receptor="{filename}"\n')  # Write the filename to the text file
        print(f'Selected file: {filename}')  # Optional: print filename to console

# Create the main application window
mGui = tk.Tk()
mGui.geometry('600x150')

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
