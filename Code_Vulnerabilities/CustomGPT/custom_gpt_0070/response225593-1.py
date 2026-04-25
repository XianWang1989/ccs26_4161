
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Opens the file dialog
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open a text file to write
            conf.write("receptor=\"{}\"\n".format(filename))  # Write the filename
        print("File saved:", filename)  # Optional: print the filename to the console

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Button to browse files
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI
mGui.mainloop()
