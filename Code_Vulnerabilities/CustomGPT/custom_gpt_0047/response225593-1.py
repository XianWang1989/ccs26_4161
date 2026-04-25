
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    filename = askopenfilename()
    if filename:  # Check if a file was selected
        with open('output.txt', 'a') as conf:  # Append to output.txt
            conf.write("receptor='{}'\n".format(filename))
        print("File selected:", filename)  # Optional: print to console

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create the Browse button and link it to the function
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI event loop
mGui.mainloop()
