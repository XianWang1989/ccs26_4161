
import tkinter as tk
from tkinter import Button
from tkinter.filedialog import askopenfilename

def browse_file():
    # This function opens the file dialog and gets the selected filename
    filename = askopenfilename()  # askopenfilename returns the selected file path
    if filename:  # Check if a file was selected
        # Write the selected file name to a text file
        with open('output.txt', 'a') as conf:  # Open output.txt in append mode
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename to the file
        print("File saved:", filename)  # Optional: print the filename to the console

# Create the main window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the Browse button and assign the browse_file function to it
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI main loop
mGui.mainloop()
