
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open file dialog to select a file
    filename = askopenfilename()
    if filename:  # check if a file was selected
        # Write the selected file name to a text file
        with open('output.txt', 'a') as conf:  # 'a' mode to append the file
            conf.write("receptor='{}'\n".format(filename))

# Set up the main GUI window
mGui = tk.Tk()
mGui.title("File Selector")

# Create a Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI main loop
mGui.mainloop()
