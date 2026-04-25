
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    # Open the file dialog and get the selected file name
    filename = filedialog.askopenfilename()
    if filename:  # Check if a file was selected
        # Write the file name to a text file
        with open("output.txt", "w") as conf:
            conf.write("receptor='{}'\n".format(filename))
        print("File saved:", filename)  # Optional: print to console

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
