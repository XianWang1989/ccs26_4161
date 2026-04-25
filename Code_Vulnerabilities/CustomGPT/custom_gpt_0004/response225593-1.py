
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Opens the file dialog
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a text file for writing
            conf.write(f'receptor="{filename}"\n')  # Write the filename to the text file
        print(f'File selected: {filename}')  # Optional: Print to console

# Set up the main application window
mGui = tk.Tk()
mGui.title("File Browser")

# Create and place the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=100, y=50)

# Run the application
mGui.mainloop()
