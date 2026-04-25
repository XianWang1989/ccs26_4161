
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open text file for writing
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename to the file
        print("Selected file:", filename)  # Optional: print the filename to console

# Create main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI main loop
mGui.mainloop()
