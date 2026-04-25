
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()  # Open the file dialog and get the selected filename
    if filename:  # Check if a file was selected
        with open('output.txt', 'w') as conf:  # Open (or create) the output file
            conf.write("receptor='{}'\n".format(filename))  # Write the filename to the file
        print("File saved:", filename)  # Print to console for confirmation

# Create the main application window
mGui = tk.Tk()
mGui.title("File Browser Example")
mGui.geometry("500x200")

# Create a button to browse files
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=200, y=50)

# Run the Tkinter event loop
mGui.mainloop()
