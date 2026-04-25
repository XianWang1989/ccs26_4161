
from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename

def browse_file():
    # Open the file dialog and get the selected filename
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        # Write the filename to a text file
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(filename))
        print("Filename saved:", filename)

# Create the main GUI window
mGui = Tk()
mGui.title("File Browser")

# Create a browse button that calls the browse_file function
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the GUI event loop
mGui.mainloop()
