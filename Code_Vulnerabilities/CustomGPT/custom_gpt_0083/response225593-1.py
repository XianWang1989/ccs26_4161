
import Tkinter as tk
from Tkinter import filedialog

# Function to open the file dialog and write the filename to a text file
def browse_file():
    filename = filedialog.askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open a file in write mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create a browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the application
mGui.mainloop()
