
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog and get the filename
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to a text file
        print("Saved:", filename)  # Optional: print to console for feedback

# Set up the main application window
mGui = tk.Tk()
mGui.title("File Selector")

# Create and place the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Start the GUI event loop
