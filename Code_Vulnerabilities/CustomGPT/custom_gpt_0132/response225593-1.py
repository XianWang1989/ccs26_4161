
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open the file dialog and get the selected filename
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:
            conf.write("receptor='{}'\n".format(filename))
        print("File saved as:", filename)

# Create the main window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI loop
mGui.mainloop()
