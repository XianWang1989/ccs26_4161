
from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Opens the file dialog and gets the filename
    if filename:  # Check if a file was selected
        with open("output.txt", "a") as conf:  # Open output.txt in append mode
            conf.write(f"receptor='{filename}'\n")  # Write the filename to the file
        print(f"Selected file: {filename}")  # Print to console for confirmation

# Create the GUI
mGui = Tk()
mGui.title("File Browser")

browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
