
import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename()  # Open file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open (or create) a text file
            conf.write(f'receptor="{filename}"\n')  # Write the filename to the file
        print(f'Selected file: {filename}')  # Print the selected filename to console

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI event loop
mGui.mainloop()
