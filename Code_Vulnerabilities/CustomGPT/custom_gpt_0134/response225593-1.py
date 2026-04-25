
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    # Open file dialog and get the file path
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        # Open your text file to write the filename
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))

# Set up the main GUI window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the main loop
mGui.mainloop()
