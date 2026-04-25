
from Tkinter import Tk, Button
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog
    if filename:  # If a file was selected
        with open("output.txt", "w") as conf:  # Open the text file in write mode
            conf.write(f"receptor='{filename}'\n")  # Write the selected filename
        print(f"File selected: {filename}")  # Optional: print the filename to the console

# Initialize the main window
mGui = Tk()
mGui.title("File Browser")

# Create a Browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
