
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    # Open file dialog
    filename = askopenfilename()

    # Write the filename to a text file
    with open('output.txt', 'w') as conf:
        conf.write(f'receptor="{filename}"\n')

    # Print the filename to console (optional)
    print(f'Selected file: {filename}')

# Create the main GUI window
mGui = tk.Tk()
mGui.title("File Browser")

# Create Browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Run the Tkinter event loop
mGui.mainloop()
