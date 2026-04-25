
import tkinter as tk
from tkinter import Button
from tkinter.filedialog import askopenfilename

def browse_file():
    # Open the file dialog and get the filename
    filename = askopenfilename()
    if filename:  # Check if a filename was selected
        # Write the filename to a text file
        with open('output.txt', 'w') as conf:
            conf.write(f'receptor="{filename}"\n')
        print(f"Selected file: {filename}")

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button and link it to the browse_file function
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI main loop
mGui.mainloop()
