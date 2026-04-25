
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog and get the file name
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))  # Write the file name to a text file
        print(f'Selected file: {filename}')  # Print the file name for confirmation

# Create the main window
mGui = tk.Tk()
mGui.geometry("500x200")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
