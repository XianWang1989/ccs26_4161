
import tkinter as tk
from tkinter import Button, filedialog

def browse_file():
    # Open the file dialog and store the selected file path
    filename = filedialog.askopenfilename()
    if filename:
        # Print the filename to a text file
        with open('output.txt', 'w') as conf:
            conf.write(f'receptor="{filename}"\n')
        print(f'Selected file: {filename}')

# Initialize the main GUI window
mGui = tk.Tk()
mGui.title("File Selector")

# Create the Browse button and link it to the function
browsebutton = Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=50, y=50)

# Run the application
mGui.mainloop()
