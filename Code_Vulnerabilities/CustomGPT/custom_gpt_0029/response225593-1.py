
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open the output file in write mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the file
        print("File saved:", filename)  # Print to console for confirmation

# Initialize the GUI
mGui = tk.Tk()
mGui.title("File Browser")

browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
