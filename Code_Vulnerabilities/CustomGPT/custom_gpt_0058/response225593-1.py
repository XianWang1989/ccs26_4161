
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # This will open the file dialog and return the selected filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open the file in write mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file
        print("File saved:", filename)  # Print the filename for confirmation

# Create the main window
mGui = Tk()
mGui.title("File Browser")

# Create the browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI
mGui.mainloop()
