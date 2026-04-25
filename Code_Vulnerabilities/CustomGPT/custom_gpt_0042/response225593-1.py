
import Tkinter as tk
from Tkinter import filedialog

def browse_file():
    # Open the file dialog and get the file name
    filename = filedialog.askopenfilename()
    # Print the file name to console (optional)
    print("Selected file:", filename)

    # Write the file name to a text file
    with open("output.txt", "w") as conf:
        conf.write("receptor='{}'\n".format(filename))

# Set up the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the main event loop
mGui.mainloop()
