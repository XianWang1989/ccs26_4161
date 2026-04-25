
import Tkinter as tk
from Tkinter import Button
from tkFileDialog import askopenfilename

def browse_file():
    # Call askopenfilename to open a file dialog and get the selected file
    filename = askopenfilename()
    if filename:  # Ensure that a file was selected
        with open('output.txt', 'a') as conf:  # Open your text file in append mode
            conf.write('receptor="{}"\n'.format(filename))  # Write the file name to the text file
        print(f'Selected file: {filename}')  # Optional: Print the selected file to the console

# Set up the GUI
mGui = tk.Tk()
mGui.title("File Browser Example")

browsebutton = Button(mGui, text='Browse', command=browse_file)  # Set the button to call browse_file
browsebutton.place(x=400, y=50)

mGui.mainloop()  # Start the GUI event loop
