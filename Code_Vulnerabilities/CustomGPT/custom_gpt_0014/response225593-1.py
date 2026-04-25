
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    # Open file dialog and get the selected file name
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        # Write the filename to the text file
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create a Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI event loop
mGui.mainloop()
