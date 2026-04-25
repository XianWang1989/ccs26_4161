
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Show file dialog and get the selected filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open a text file for writing
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file

# Create the main GUI window
mGui = Tk()
mGui.title("File Browser")

# Create and place the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
