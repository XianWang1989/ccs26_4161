
import Tkinter as tk
from Tkinter import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open dialog to select a file
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write('receptor="{}"\n'.format(filename))  # Write filename to output.txt

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create a button that calls the browse_file function
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI
mGui.mainloop()
