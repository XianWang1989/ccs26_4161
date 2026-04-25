
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog and get the filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Open a text file in append mode
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the text file
        print("File selected:", filename)  # Optionally print the filename to the console

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Selector")
mGui.geometry("500x200")

# Create the browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=200, y=50)  # Position the button

# Start the Tkinter event loop
mGui.mainloop()
