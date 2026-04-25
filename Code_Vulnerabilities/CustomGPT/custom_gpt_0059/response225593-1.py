
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open file to write
            conf.write('receptor="{}"\n'.format(filename))  # Write the filename
        print("File saved to output.txt")

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.pack(pady=20)

# Start the main loop
mGui.mainloop()
