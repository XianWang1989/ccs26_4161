
import Tkinter as tk  # Import Tkinter for Python 2.5
from tkFileDialog import askopenfilename

def browse_file():
    # Open file dialog and get the selected file name
    file_name = askopenfilename()
    if file_name:  # Check if a file was selected
        with open("output.txt", "w") as conf:
            conf.write('receptor="{}"\n'.format(file_name))  # Write the file name to output.txt
        print("File name saved:", file_name)  # Optional: Print to console for confirmation

# Create main window
mGui = tk.Tk()
mGui.title("File Browser")

# Create browse button
browsebutton = tk.Button(mGui, text='Browse', command=browse_file)
browsebutton.place(x=400, y=50)

# Start the GUI main loop
mGui.mainloop()
