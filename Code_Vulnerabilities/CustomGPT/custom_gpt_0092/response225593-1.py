
import tkinter as tk
from tkinter import Button, filedialog

def browse_file():
    filename = filedialog.askopenfilename()  # Open file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a file to write
            conf.write(f'receptor="{filename}"\n')  # Write filename to the text file
        print(f'Selected file: {filename}')  # Print the filename to the console

# Create the main application window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Start the GUI event loop
