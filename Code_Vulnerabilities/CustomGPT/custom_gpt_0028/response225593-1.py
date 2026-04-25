
from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename

def browse_file():
    # Open file dialog and get the file name
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open a text file to write the file name
            conf.write("receptor='{}'\n".format(filename))  # Write the file name to the text file
        print("File name saved to output.txt")

mGui = Tk()
mGui.title("File Browser")

browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()
