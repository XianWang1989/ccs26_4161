
import Tkinter as tk
from tkFileDialog import askopenfilename

# Create a simple GUI
def browse_file():
    filename = askopenfilename()  # Open the file dialog to select a file
    if filename:  # Check if a file was selected
        with open("output.txt", "a") as conf:  # Open a text file in append mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file
        print("File selected: ", filename)  # Optional: print the filename to console

# Initialize the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create a Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
