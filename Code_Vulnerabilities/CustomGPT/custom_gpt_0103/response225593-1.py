
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open file dialog to select a file
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open a text file to write
            conf.write(f'receptor="{filename}"\n')  # Write the filename to the text file

# Create the main GUI window
mGui = Tk()

# Create a "Browse" button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI loop
mGui.mainloop()
