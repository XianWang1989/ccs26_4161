
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog and return the selected filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open the text file in write mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the file
        print("File saved:", filename)  # Print confirmation to the console

# Create the main GUI window
mGui = Tk()
mGui.title("File Selector")

# Create the Browse button and set its command to the browse_file function
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Run the GUI
