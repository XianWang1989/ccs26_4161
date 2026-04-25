
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog and get the filename
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open the text file for writing
            conf.write(f'receptor="{filename}"\n')  # Write the filename to the file
        print("File saved:", filename)  # Optionally print to the console

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create and place the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the main event loop
mGui.mainloop()
