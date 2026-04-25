
import tkinter as tk
from tkinter import Button, filedialog

def browse_file():
    # Open file dialog and retrieve the selected file name
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        # Write the filename to a text file
        with open('output.txt', 'w') as conf:
            conf.write(f"receptor='{filename}'\n")
        print(f'Selected file: {filename}')  # Optional: print to console

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI event loop
mGui.mainloop()
