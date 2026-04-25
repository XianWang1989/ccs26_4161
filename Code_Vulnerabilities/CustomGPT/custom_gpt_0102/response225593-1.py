
import Tkinter as tk
from tkFileDialog import askopenfilename

def browse_file():
    file_path = askopenfilename()
    if file_path:  # Check if a file was selected
        with open('output.txt', 'w') as conf:
            conf.write("receptor='{}'\n".format(file_path))

# Create the main application window
mGui = tk.Tk()
mGui.title("File Chooser")

# Create browse button
browse_button = tk.Button(mGui, text='Browse', command=browse_file)
browse_button.place(x=400, y=50)

# Start the GUI main loop
mGui.mainloop()
