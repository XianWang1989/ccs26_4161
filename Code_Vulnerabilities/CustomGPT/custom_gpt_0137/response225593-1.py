
import Tkinter as tk
from Tkinter import Button
from tkFileDialog import askopenfilename

def browse_file():
    # This function is called when the button is pressed
    filename = askopenfilename()  # Open file dialog and get the selected file path
    if filename:  # Check if a file was selected
        with open("output.txt", "w") as conf:  # Open the output file in write mode
            conf.write("receptor='{}'\n".format(filename))  # Write the file path to the text file
        print("File selected:", filename)  # Print the selected file name for confirmation

# Create the main window
mGui = tk.Tk()
mGui.title("File Browser")
mGui.geometry("600x400")

# Create the Browse button
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Start the Tkinter main loop
